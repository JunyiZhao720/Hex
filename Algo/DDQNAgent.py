import gym
import tensorflow as tf
from collections import deque

import random
import numpy as np
import math

from tensorflow.keras import Model, Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Input
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import Huber
from tensorflow.keras.initializers import he_normal
from tensorflow.keras.callbacks import History


class DDQNAgent:
    MAX_EPSILON = 1
    MIN_EPSILON = 0.01

    GAMMA = 0.95
    LAMBDA = 0.0005
    TAU = 0.08

    REWARD_STD = 1.0

    def __init__(self, experience_replay, state_shape, actions_size, batch_size, optimizer):

        # Initialize attributes
        self._state_shape = state_shape
        self._action_size = actions_size
        self._optimizer = optimizer
        self._batch_size = batch_size

        self.experience_replay = experience_replay

        # Initialize discount and exploration rate
        self.epsilon = DDQNAgent.MAX_EPSILON

        # Build networks
        self.primary_network = self._build_network()
        self.primary_network.compile(loss='mse', optimizer=self._optimizer)

        self.target_network = self._build_network()

    def _build_network(self):
        network = Sequential()
        #network.add(Conv2D(32, 2, 1, padding='valid', activation='relu'))
        network.add(Flatten(input_shape=self._state_shape))
        network.add(Dense(32, activation='relu'))
        network.add(Dense(32, activation='relu'))
        network.add(Dense(self._action_size))

        return network

    def align_epsilon(self, step):
        self.epsilon = DDQNAgent.MIN_EPSILON + (DDQNAgent.MAX_EPSILON - DDQNAgent.MIN_EPSILON) * math.exp(-DDQNAgent.LAMBDA * step)

    def align_target_network(self):
        for t, e in zip(self.target_network.trainable_variables,
                        self.primary_network.trainable_variables): t.assign(t * (1 - DDQNAgent.TAU) + e * DDQNAgent.TAU)

    def act(self, observation):
        if np.random.rand() < self.epsilon:
            return np.random.randint(0, self._action_size)
        else:
            q_values = self.primary_network.predict(x=np.reshape(observation['state'], (-1, self._state_shape[0],  self._state_shape[1])))
            return np.argmax(q_values)

    def store(self, observation, action, reward, next_observation, terminated):
        self.experience_replay.store(observation, action, reward, next_observation, terminated)

    def train(self, batch_size):
        if self.experience_replay.buffer_size < self._batch_size * 3:
            return 0

        batch = self.experience_replay.get_batch(batch_size)
        observations, actions, rewards, next_observations = self.experience_replay.get_arrays_from_batch(batch)
        states = np.reshape([observation['state'] for observation in observations], (-1, self._state_shape[0],  self._state_shape[1]))
        next_states = np.reshape([observation['state'] for observation in next_observations], (-1, self._state_shape[0],  self._state_shape[1]))

        # Predict Q(s,a) and Q(s',a') given the batch of states
        q_values_state = self.primary_network(states).numpy()
        q_values_next_state = self.primary_network(next_states).numpy()

        # Copy the q_values_state into the target
        target = q_values_state
        updates = np.zeros(rewards.shape)

        valid_indexes = next_states.reshape(-1, self._state_shape[0]*self._state_shape[1]).sum(axis=1) != 0
        batch_indexes = np.arange(self._batch_size)

        action = np.argmax(q_values_next_state, axis=1)
        q_next_state_target = self.target_network(next_states)
        updates[valid_indexes] = rewards[valid_indexes] + DDQNAgent.GAMMA * q_next_state_target.numpy()[batch_indexes[valid_indexes], action[valid_indexes]]

        target[batch_indexes, actions] = updates
        loss = self.primary_network.train_on_batch(states, target)

        # update target network parameters slowly from primary network
        self.align_target_network()

        return loss