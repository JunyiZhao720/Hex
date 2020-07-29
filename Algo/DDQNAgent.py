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

    BATCH_SIZE = 32
    REWARD_STD = 1.0

    def __init__(self, experience_replay, state_size, actions_size, optimizer):

        # Initialize attributes
        self._state_size = state_size
        self._action_size = actions_size
        self._optimizer = optimizer

        self.experience_replay = experience_replay

        # Initialize discount and exploration rate
        self.epsilon = DDQNAgent.MAX_EPSILON

        # Build networks
        self.primary_network = self._build_network()
        self.primary_network.compile(loss='mse', optimizer=self._optimizer)

        self.target_network = self._build_network()

    def _build_network(self):
        network = Sequential()
        network.add(Dense(30, activation='relu', kernel_initializer=he_normal()))
        network.add(Dense(30, activation='relu', kernel_initializer=he_normal()))
        network.add(Dense(self._action_size))

        return network

    def align_epsilon(self, step):
        self.epsilon = DDQNAgent.MIN_EPSILON + (DDQNAgent.MAX_EPSILON - DDQNAgent.MIN_EPSILON) * math.exp(-DDQNAgent.LAMBDA * step)

    def align_target_network(self):
        for t, e in zip(self.target_network.trainable_variables,
                        self.primary_network.trainable_variables): t.assign(t * (1 - DDQNAgent.TAU) + e * DDQNAgent.TAU)

    def act(self, state):
        if np.random.rand() < self.epsilon:
            return np.random.randint(0, self._action_size - 1)
        else:
            q_values = self.primary_network(state.reshape(1, -1))
            return np.argmax(q_values)

    def store(self, state, action, reward, next_state, terminated):
        self.expirience_replay.store(state, action, reward, next_state, terminated)

    def train(self, batch_size):
        if self.expirience_replay.buffer_size < DDQNAgent.BATCH_SIZE * 3:
            return 0

        batch = self.expirience_replay.get_batch(batch_size)
        states, actions, rewards, next_states = expirience_replay.get_arrays_from_batch(batch)

        # Predict Q(s,a) and Q(s',a') given the batch of states
        q_values_state = self.primary_network(states).numpy()
        q_values_next_state = self.primary_network(next_states).numpy()

        # Copy the q_values_state into the target
        target = q_values_state
        updates = np.zeros(rewards.shape)

        valid_indexes = np.array(next_states).sum(axis=1) != 0
        batch_indexes = np.arange(DDQNAgent.BATCH_SIZE)

        action = np.argmax(q_values_next_state, axis=1)
        q_next_state_target = self.target_network(next_states)
        updates[valid_indexes] = rewards[valid_indexes] + DDQNAgent.GAMMA * q_next_state_target.numpy()[batch_indexes[valid_indexes], action[valid_indexes]]

        target[batch_indexes, actions] = updates
        loss = self.primary_network.train_on_batch(states, target)

        # update target network parameters slowly from primary network
        self.align_target_network()

        return loss