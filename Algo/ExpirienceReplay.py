import random
from collections import deque

import numpy as np

class ExpirienceReplay:
    def __init__(self, maxlen=2000):
        self._buffer = deque(maxlen=maxlen)

    def store(self, observation, action, reward, next_observation, terminated):
        self._buffer.append((observation, action, reward, next_observation, terminated))

    def get_batch(self, batch_size):
            return random.sample(self._buffer, batch_size)

    def get_arrays_from_batch(self, batch):
        observations = np.array([x[0] for x in batch])
        actions = np.array([x[1] for x in batch])
        rewards = np.array([x[2] for x in batch])
        next_observations = np.array([x[3] for x in batch])

        return observations, actions, rewards, next_observations

    @property
    def buffer_size(self):
        return len(self._buffer)