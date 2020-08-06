import numpy as np
import tensorflow as tf
from HexEngine import HexEngine
from HexGui import HexGui


from tf_agents.policies import random_py_policy

class HexEnv():
    def __init__(self):
        self._engine = None
        self._actions = None
        self._state = None
        self._episode_ended = None
        self._verbose = True

    # Constructors
    @staticmethod
    def create_new(n, human_color_red, human_move_first, ai, verbose=True):
        instance = HexEnv()
        engine = HexEngine.create_new(n, human_color_red, human_move_first, HexGui(human_color_red), ai)
        instance._engine = engine
        instance._actions = np.arange(1, engine.n**2 + 1)
        instance._state = engine.board
        instance._episode_ended = False
        instance._verbose = verbose
        return instance

    @staticmethod
    def create_from_engine(engine, verbose=True):
        instance = HexEnv()
        instance._engine = engine
        instance._actions = np.arange(1, engine.n**2 + 1)
        instance._state = engine.board
        instance._episode_ended = False
        instance._verbose = verbose
        return instance

    # manipulation methods
    def _get_mask(self):
        mask = np.zeros((self._engine.n**2,), dtype=np.int32)
        a = self._engine.available_encoded_moves()
        for i in self._engine.available_encoded_moves():
            mask[i] = 1
        return mask


    # get n * n board rather than n+1 * n+1
    def _get_state(self):
        return np.array([row[1:] for row in self._engine.board[1:]], dtype=np.int32)

    # return: observation = {state:, mask:, }
    def reset(self):
        self._engine.reset()
        self._episode_ended = False
        self._state = self._get_state()
        return {'state': np.array(self._state, dtype=np.int32), 'mask': self._get_mask()}

    # return: reward, next_observation, termination
    def step(self, action):
        if self._episode_ended:
            return self.reset()

        self._engine.move(action, useGui=self._verbose)

        if self._engine.wining_check():
            self._episode_ended = True

        self._state = self._get_state()

        if self._episode_ended:
            return ({'state': self._state, 'mask': self._get_mask()}), 1.0, True
        else:
            return ({'state': self._state, 'mask': self._get_mask()}), 0.0, False

    def actions(self):
        return self._actions

if __name__ == '__main__':
    pass
    #para = (8, False, True, True, 'Monte', 'Monte', 1, 2)
    # gui = HexGui(human_color_red=para[2])
    # engine = HexEngine.create_new(n=para[0], human_color_red=para[2], human_move_first=para[3], gui=gui, ai=None)
    # env = HexEnv(engine)
    # #utils.validate_py_environment(env, episodes=1)
    #
    # random_policy = random_py_policy.RandomPyPolicy(time_step_spec=env.time_step_spec(), action_spec=env.action_spec(), observation_and_action_constraint_splitter=HexEnv.observation_and_action_constraint_splitter)
    # time_step = env.reset()
    #
    # episode_count = 0
    # episode = 1
    #
    # while episode_count < episode:
    #     action = random_policy.action(time_step).action
    #     time_step = env.step(action)
    #
    #     if time_step.is_last():
    #         episode_count += 1
    #         time_step = env.reset()


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