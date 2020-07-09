import numpy as np
import time
from HexEngine import HexEngine


class HexAI:

    @staticmethod
    def MonteCarlo(AI_color):
        return MonteCarlo(AI_color)

    @staticmethod
    def DDQN():
        return DDQN()

class MonteCarlo:
    def __init__(self, AI_color):
        self.AI_color = AI_color
        self.engine = None


    # Play current single move
    # Return 1 if AI wins
    # Return 0 if AI loses
    def _play_single(self, point, engine_copy):
        engine_copy.move(point)

        moves = engine_copy.available_moves()
        n = len(moves)
        for i in range(n):
            # Check wining
            win_result  = engine_copy.wining_check()
            if win_result != 0:
                if win_result == self.AI_color:
                    return 1
                else:
                    return 0
            # Next move
            move_index = np.random.randint(0, len(moves))
            point = moves[move_index]
            moves.remove(point)
            engine_copy.move(point)

    # Play multi-processing moves
    # TODO multi-processing
    def _play(self, point, engine, n=10, n_jobs=1):
        result = 0
        for i in range(n):
            result += self._play_single(point=point, engine_copy=engine.copy())

        return result / (n * n_jobs)


    def solve(self, engine, verbose=False):
        self.engine = engine
        moves = engine.available_moves()
        prob = np.zeros((1, len(moves)))

        time_used= time.time()
        for i in range(len(moves)):
            prob[i] = self._play(point=moves[i], engine=engine)

        time_used = time.time() - time_used
        if verbose:
            print("MonteCarlo used " + str(time_used) + " seconds to solve the answer!")
        return moves[np.argmax(prob)]





class DDQN:
    def solve(self, engine):
        pass


if __name__ == '__main__':

    model = HexEngine.create_exist(board=None, human_color_red=True, round=2, useGui = False)
    print('Hello World')