
from HexEngine import HexEngine
from Algorithms.MonteCarlo import MonteCarlo
from Algorithms.DDQN import DDQN

class HexAI:

    @staticmethod
    def MonteCarlo(AI_color):
        return MonteCarlo(AI_color)

    @staticmethod
    def DDQN():
        return DDQN()

if __name__ == '__main__':
    solver = HexAI.MonteCarlo(AI_color=2)
    model = HexEngine.create_exist(board=HexEngine.init_board(n=5), human_color_red=True, round=2, useGui = False)

    print('Hello World')