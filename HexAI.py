

from model.MonteCarlo import MonteCarlo

class HexAI:

    @staticmethod
    def MonteCarlo(AI_color):
        return MonteCarlo(AI_color)

    @staticmethod
    def DDQN():
        return DDQN()

if __name__ == '__main__':
    # solver = HexAI.MonteCarlo(AI_color=2)
    # engine = HexEngine.create_exist(board=HexEngine.init_board(n=5), human_color_red=True, round=2, gui=None, ai=None)
    # solver.solve(engine=engine, verbose=True)

    print('Hello World')