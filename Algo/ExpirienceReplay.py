import random
from collections import deque

import numpy as np

class ExpirienceReplay:
    def __init__(self, maxlen=2000):
        self._buffer = deque(maxlen=maxlen)

    def store(self, state, action, reward, next_state, terminated):
        self._buffer.append((state, action, reward, next_state, terminated))

    def get_batch(self, batch_size):
        if no_samples > len(self._samples):
            return random.sample(self._buffer, len(self._samples))
        else:
            return random.sample(self._buffer, batch_size)

    def get_arrays_from_batch(self, batch):
        states = np.array([x[0] for x in batch])
        actions = np.array([x[1] for x in batch])
        rewards = np.array([x[2] for x in batch])
        next_states = np.array([(np.zeros(NUM_STATES) if x[3] is None else x[3])
                                for x in batch])

        return states, actions, rewards, next_states

    @property
    def buffer_size(self):
        return len(self._buffer)