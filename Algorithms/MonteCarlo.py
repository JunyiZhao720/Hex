import numpy as np
import time
from multiprocessing import Pool

class MonteCarlo:
    def __init__(self, AI_color, move_iter = 100, n_jobs=2):
        self.AI_color = AI_color
        self.engine = None
        self.move_iter = move_iter
        self.n_jobs = n_jobs

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
            if win_result:
                if win_result == self.AI_color:
                    return 1
                else:
                    return 0
            # Next move
            move_index = np.random.randint(0, len(moves))
            point = moves[move_index]
            moves.remove(point)
            engine_copy.move(point)

        print('Warning: MonteCarlo._play_single runs out of moves, will return 0.')

        return 0

    # Play multi-processing moves
    def _play(self, point, engine):
        with Pool(self.n_jobs) as pool:
            results = pool.starmap(self._play_single, [[point, engine.clone()] for i in range(self.move_iter)])
            pool.close()
            pool.join()
        return sum(results) / self.move_iter

    #-------------------------------------PUBLIC FIELD-----------------------------------------

    def clone(self):
        instance = MonteCarlo(self.AI_color)
        instance.engine = self.engine.clone(useGui = True, useAI = True)

        return instance

    def solve(self, engine, verbose=False):
        self.engine = engine
        moves = engine.available_moves()
        prob = np.zeros((len(moves), 1))

        time_used= time.time()
        for i in range(len(moves)):
            prob[i] = self._play(point=moves[i], engine=engine)

        time_used = time.time() - time_used
        print(prob)
        if verbose:
            print("MonteCarlo used " + str(time_used) + " seconds to solve the answer!")
        return moves[np.argmax(prob)]