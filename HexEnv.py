import numpy as np
import tensorflow as tf
from HexEngine import HexEngine
from HexGui import HexGui


from tf_agents.environments import py_environment
from tf_agents.environments import tf_environment
from tf_agents.environments import tf_py_environment
from tf_agents.environments import utils
from tf_agents.specs import array_spec
from tf_agents.environments import wrappers
from tf_agents.environments import suite_gym
from tf_agents.trajectories import time_step as ts
from tf_agents.policies import random_py_policy

class HexEnv(py_environment.PyEnvironment):
    def __init__(self, engine):
        super().__init__()
        self._engine = engine
        #self._action_spec = array_spec.BoundedArraySpec.from_array(np.arange(1, self._engine.n**2 + 1).astype(np.int32), name='action')
        self._action_spec = array_spec.BoundedArraySpec(minimum=1, maximum=self._engine.n**2, shape=(), dtype=np.int32, name='action')
        self._observation_spec = {
            'state': array_spec.BoundedArraySpec(
            shape=(engine.n + 1,engine.n + 1), dtype=np.int32, minimum=0, maximum=2, name='state'),
            'mask': array_spec.BoundedArraySpec(
            shape=(self._engine.n**2,), dtype=np.int32, minimum=0, maximum=1, name='mask')
        }
        self._state = engine.board
        self._episode_ended = False

    def _get_mask(self):
        mask = np.zeros((self._engine.n**2,), dtype=np.int32)
        for i in self._engine.available_encoded_moves():
            mask[i - 1] = 1
        return mask

    # Used for mask extraction
    @staticmethod
    def observation_and_action_constraint_splitter(observation):
        return observation, tf.convert_to_tensor(observation['mask'], dtype=np.int32)

    def reset(self):
        self._engine.reset()
        self._episode_ended = False
        self._state = self._engine.board
        return ts.restart({'state': np.array(self._state, dtype=np.int32), 'mask': self._get_mask()})

    def step(self, action):

        if self._episode_ended:
            return self.reset()

        self._engine.move(action)

        if self._engine.wining_check():
            self._episode_ended = True
        else:
            self._state = self._engine.board

        if self._episode_ended:
            return ts.termination(({'state': np.array(self._state, dtype=np.int32), 'mask': self._get_mask()}), 1.0)
        else:
            return ts.transition(({'state': np.array(self._state, dtype=np.int32), 'mask': self._get_mask()}), reward=0.0, discount=1.0)

    def action_spec(self):
        return self._action_spec

    def observation_spec(self):
        return self._observation_spec


if __name__ == '__main__':
    para = (8, False, True, True, 'Monte', 'Monte', 1, 2)
    gui = HexGui(human_color_red=para[2])
    engine = HexEngine.create_new(n=para[0], human_color_red=para[2], human_move_first=para[3], gui=gui, ai=None)
    env = HexEnv(engine)
    #utils.validate_py_environment(env, episodes=1)

    random_policy = random_py_policy.RandomPyPolicy(time_step_spec=env.time_step_spec(), action_spec=env.action_spec(), observation_and_action_constraint_splitter=HexEnv.observation_and_action_constraint_splitter)
    time_step = env.reset()

    episode_count = 0
    episode = 1

    while episode_count < episode:
        action = random_policy.action(time_step).action
        time_step = env.step(action)

        if time_step.is_last():
            episode_count += 1
            time_step = env.reset()


    # environment = env
    # time_step = environment.reset()
    # print(time_step)
    # cumulative_reward = time_step.reward
    #
    # for _ in range(500):
    #     time_step = environment.step(np.random.randint(1, 65))
    #     print(time_step)
    #     cumulative_reward += time_step.reward
    #
    # time_step = environment.step(np.random.randint(1, 65))
    # print(time_step)
    # cumulative_reward += time_step.reward
    # print('Final Reward = ', cumulative_reward)