from pyspark import SparkContext, SparkConf
import random


class MonteCarlo:
    # threshold  = len(moves) * len(threads)
    def __init__(self, n_copies):
        self.sc = SparkContext(appName="MonteCarloSpark", master="local[6]", conf=SparkConf().set('spark.ui.port', random.randrange(4000,5000)))
        self.n_copies = n_copies

    # start from 0
    def _encodePoint(self, coordinate, n):
        return n * (coordinate[0] - 1) + coordinate[1] - 1

    # start from (1, 1)
    def _decodePoint(self, point, n):
        if type(point) is tuple:
            return point
        elif type(point) is not int:
            print('_decode error:', type(point))
            return (-1, -1)
        row = point // n + 1
        col = point % n + 1
        return (row, col)

    def _adjNodes(self, point, n):
        result = []
        coordinate = self._decodePoint(point, n)
        if coordinate[0] - 1 >= 1 and coordinate[1] - 1 >= 1:
            result.append((coordinate[0] - 1, coordinate[1] - 1))
        if coordinate[0] - 1 >= 1:
            result.append((coordinate[0] - 1, coordinate[1]))
        if coordinate[1] - 1 >= 1:
            result.append((coordinate[0], coordinate[1] - 1))
        if coordinate[1] + 1 <= n:
            result.append((coordinate[0], coordinate[1] + 1))
        if coordinate[0] + 1 <= n:
            result.append((coordinate[0] + 1, coordinate[1]))
        if coordinate[0] + 1 <= n and coordinate[1] + 1 <= n:
            result.append((coordinate[0] + 1, coordinate[1] + 1))

        return [self._encodePoint(point, n) for point in result]

    def _bfs(self, state):
        n = len(state) - 1
        # Check Player 1
        queue = []
        visited = [[False] * (n + 1) for i in range(n + 1)]
        for i in range(1, n + 1):
            if state[1][i] == 1:
                queue.append(self._encodePoint((1, i), n))
                visited[1][i] = True
        while queue:
            s = queue.pop(0)
            s_temp = self._decodePoint(s, n)
            s_color = state[s_temp[0]][s_temp[1]]
            adj_nodes = self._adjNodes(s, n)
            for node in adj_nodes:
                temp = self._decodePoint(node, n)
                if state[temp[0]][temp[1]] == s_color and not visited[temp[0]][temp[1]]:
                    queue.append(node)
                    visited[temp[0]][temp[1]] = True
        for i in range(1, n + 1):
            if visited[n][i]:
                return 1

        # Check Player 2
        queue = []
        visited = [[False] * (n + 1) for i in range(n + 1)]
        for i in range(1, n + 1):
            if state[i][1] == 2:
                queue.append(self._encodePoint((i, 1), n))
                visited[i][1] = True
        while queue:
            s = queue.pop(0)
            s_temp = self._decodePoint(s, n)
            s_color = state[s_temp[0]][s_temp[1]]
            adj_nodes = self._adjNodes(s, n)
            for node in adj_nodes:
                temp = self._decodePoint(node, n)
                if state[temp[0]][temp[1]] == s_color and not visited[temp[0]][temp[1]]:
                    queue.append(node)
                    visited[temp[0]][temp[1]] = True
        for i in range(1, n + 1):
            if visited[i][n]:
                return 2

        return None

    def _availableMoves(self, state):
        n = len(state) - 1
        moves = {}
        for x in range(1, n + 1):
            for y in range(1, n + 1):
                if not state[x][y]:
                    moves[(x, y)] = 0
        return moves

    def _flip_index(self, index):
        if index == 1:
            return 2
        else:
            return 1

    def _solve_task(self, task):
        moves = task[0]
        state = task[1]
        index = task[2]
        task_result = []

        for move in moves:
            s = [*state]
            m = set(moves.keys())
            s[move[0]][move[1]] = index
            m.remove(move)
            i = self._flip_index(index)

            for _ in range(len(m)):
                _m = random.choice(tuple(m))
                s[_m[0]][_m[1]] = i
                m.remove(_m)
                i = self._flip_index(i)

            # win check
            result = self._bfs(s)
            if result == index:
                task_result.append((move, 1))
            else:
                task_result.append((move, 0))

        return task_result




    def solve(self, index, state):
        # Prepare for Tasks
        moves = self._availableMoves(state)
        tasks = [(moves, state, index)] * self.n_copies

        # Spark Copy
        # data = self.sc.parallelize(tasks)
        # data = data.flatMap(lambda task: self._solve_task(task))
        data = self._solve_task(tasks[0])
        print(data)


        return (1,1)
