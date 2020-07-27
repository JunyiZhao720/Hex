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

class HexEnv(py_environment.PyEnvironment):
    def __init__(self, engine):
        super().__init__()
        self._engine = engine
        self._action_spec = array_spec.BoundedArraySpec(
            shape=(), dtype=np.int32, minimum=1, maximum=self._engine.n**2, name = 'action')
        # TODO
        self._observation_spec = array_spec.BoundedArraySpec(
            shape=(engine.n + 1,engine.n + 1), dtype=np.int32, minimum=0, maximum=2, name='observation')
        self._state = engine.board
        self._episode_ended = False

    def action_spec(self):
        return self._action_spec

    def observation_spec(self):
        return self._observation_spec

    def _reset(self):
        self._engine.reset()
        self._episode_ended = False
        # TODO
        return ts.restart(self._engine.board)

    def _step(self, action):

        if self._episode_ended:
            return self.reset()

        self._engine.move(action)

        if self._engine.wining_check():
            self._episode_ended = True
        else:
            self._state = self._engine.board
        if self._episode_ended:
            return ts.termination(np.array(self._state, dtype=np.int32), 1.0)
        else:
            return ts.transition(np.array(self._state, dtype=np.int32), reward=0.0, discount=1.0)



if __name__ == '__main__':
    para = (8, False, True, True, 'Monte', 'Monte', 1, 2)
    gui = HexGui(human_color_red=para[2])
    engine = HexEngine.create_new(n=para[0], human_color_red=para[2], human_move_first=para[3], gui=gui, ai=None)
    env = HexEnv(engine)
    utils.validate_py_environment(env, episodes=5)