class BFS:
    # start from 0
    @staticmethod
    def _encodePoint(coordinate, n):
        return n * (coordinate[0] - 1) + coordinate[1] - 1

    # start from (1, 1)
    @staticmethod
    def _decodePoint(point, n):
        if type(point) is tuple:
            return point
        elif type(point) is not int:
            print('_decode error:', type(point))
            return (-1, -1)
        row = point // n + 1
        col = point % n + 1
        return (row, col)

    @staticmethod
    def _adjNodes(point, n):
        result = []
        coordinate = BFS._decodePoint(point, n)
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

        return [BFS._encodePoint(point, n) for point in result]

    @staticmethod
    def bfs(state):
        n = len(state) - 1
        # Check Player 1
        queue = []
        visited = [[False] * (n + 1) for i in range(n + 1)]
        for i in range(1, n + 1):
            if state[1][i] == 1:
                queue.append(BFS._encodePoint((1, i), n))
                visited[1][i] = True
        while queue:
            s = queue.pop(0)
            s_temp = BFS._decodePoint(s, n)
            s_color = state[s_temp[0]][s_temp[1]]
            adj_nodes = BFS._adjNodes(s, n)
            for node in adj_nodes:
                temp = BFS._decodePoint(node, n)
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
                queue.append(BFS._encodePoint((i, 1), n))
                visited[i][1] = True
        while queue:
            s = queue.pop(0)
            s_temp = BFS._decodePoint(s, n)
            s_color = state[s_temp[0]][s_temp[1]]
            adj_nodes = BFS._adjNodes(s, n)
            for node in adj_nodes:
                temp = BFS._decodePoint(node, n)
                if state[temp[0]][temp[1]] == s_color and not visited[temp[0]][temp[1]]:
                    queue.append(node)
                    visited[temp[0]][temp[1]] = True
        for i in range(1, n + 1):
            if visited[i][n]:
                return 2

        return None