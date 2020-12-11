class BFS:
    # start from 0
    @staticmethod
    def _encodePoint(point, n):
        return n * (point[0] - 1) + point[1] - 1

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
    def adjNodes(point, n):
        result = []
        r = point[0]
        c = point[1]
        # left top
        if r - 1 >= 1:
            result.append((r - 1, c))
        # right top
        if r - 1 >= 1 and c + 1 <= n:
            result.append((r - 1, c + 1))
        # left middle
        if c - 1 >= 1:
            result.append((r, c - 1))
        # right middle
        if c + 1 <= n:
            result.append((r, c + 1))
        # left bottom
        if r + 1 <= n and c - 1 >= 1:
            result.append((r + 1, c - 1))
        # right bottom
        if r + 1 <= n:
            result.append((r + 1, c))

        return result

    @staticmethod
    def bfs(state):
        n = len(state) - 1
        # Check Player 1
        queue = []
        visited = [[False] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            if state[1][i] == 1:
                queue.append((1, i))
                visited[1][i] = True
        while queue:
            s = queue.pop(0)
            s_color = state[s[0]][s[1]]
            adj_nodes = BFS.adjNodes(s, n)
            for node in adj_nodes:
                if state[node[0]][node[1]] == s_color and not visited[node[0]][node[1]]:
                    queue.append(node)
                    visited[node[0]][node[1]] = True
        for i in range(1, n + 1):
            if visited[n][i]:
                return 1

        # Check Player 2
        queue = []
        visited = [[False] * (n + 1) for i in range(n + 1)]
        for i in range(1, n + 1):
            if state[i][1] == 2:
                queue.append((i, 1))
                visited[i][1] = True
        while queue:
            s = queue.pop(0)
            s_color = state[s[0]][s[1]]
            adj_nodes = BFS.adjNodes(s, n)
            for node in adj_nodes:
                if state[node[0]][node[1]] == s_color and not visited[node[0]][node[1]]:
                    queue.append(node)
                    visited[node[0]][node[1]] = True
        for i in range(1, n + 1):
            if visited[i][n]:
                return 2

        return None