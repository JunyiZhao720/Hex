from pyspark import SparkContext, SparkConf
from spark.model.BFS import BFS
import random
import time

class MonteCarlo:
    # threshold  = len(moves) * len(threads)
    def __init__(self, n_copies):
        self.sc = SparkContext(appName="MonteCarloSpark", master="local[6]", conf=SparkConf().set('spark.ui.port', random.randrange(4000,5000)))
        self.n_copies = n_copies

    def _availableMoves(self, state):
        n = len(state) - 1
        moves = {}
        for x in range(1, n + 1):
            for y in range(1, n + 1):
                if not state[x][y]:
                    moves[(x, y)] = 0
        return moves

    @staticmethod
    def _flip_index(index):
        if index == 1:
            return 2
        else:
            return 1

    @staticmethod
    def _solve_task(task):
        moves = task[0]
        state = task[1]
        index = task[2]
        task_result = []

        for move in moves:
            s = [[*row] for row in state]
            m = set(moves.keys())
            s[move[0]][move[1]] = index
            m.remove(move)
            i = MonteCarlo._flip_index(index)

            for _ in range(len(m)):
                _m = random.choice(tuple(m))
                s[_m[0]][_m[1]] = i
                m.remove(_m)
                i = MonteCarlo._flip_index(i)

            # win check
            result = BFS.bfs(s)
            if result == index:
                task_result.append((move, 1))
            else:
                task_result.append((move, 0))

        return task_result


    def solve(self, index, state):
        # Prepare for Tasks
        moves = self._availableMoves(state)
        tasks = [(moves, state, index)] * self.n_copies
        # Spark
        data = self.sc.parallelize(tasks)
        data = data.flatMap(lambda task: MonteCarlo._solve_task(task))
        data = data.reduceByKey(lambda x,y: x+y)
        data = data.sortBy(lambda x:x[1], False)
        data = data.take(1)

        return data[0][0]
