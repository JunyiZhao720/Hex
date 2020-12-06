
from HexGui import HexGui
from HexAI import HexAI

import numpy as np
class HexEngine:
    # When constructing the class, use HexEngine.create_new()
    # When need copying, use HexEngine.create_exist()
    # Notice the default constructor should not be used explicitly!!!
    def __init__(self, n, player1, player2, gui, player1First = True):
        self.n = n
        self.players = {}
        self.players[1] = player1
        self.players[2] = player2
        self.gui = gui
        self.board = np.zeros((n+1, n+1), dtype=np.int32)
        if player1First:
            self.round = self.players[1]
        else:
            self.round = self.players[2]

    # start from 0
    def _encodePoint(self, coordinate):
        return self.n * (coordinate[0] - 1) + coordinate[1] - 1

    # start from (1, 1)
    def _decodePoint(self, point):
        if type(point) is tuple:
            return point
        elif type(point) is not int:
            print('_decode error:', type(point))
            return (-1, -1)
        row = point // self.n + 1
        col = point % self.n + 1
        return (row, col)

    def _adjNodes(self, point):
        result = []
        coordinate = self._decodePoint(point)
        if coordinate[0] - 1 >= 1 and coordinate[1] - 1 >= 1:
            result.append((coordinate[0] - 1, coordinate[1] - 1))
        if coordinate[0] - 1 >= 1:
            result.append((coordinate[0] - 1, coordinate[1]))
        if coordinate[1] - 1 >= 1:
            result.append((coordinate[0], coordinate[1] - 1))
        if coordinate[1] + 1 <= self.n:
            result.append((coordinate[0], coordinate[1] + 1))
        if coordinate[0] + 1 <= self.n:
            result.append((coordinate[0] + 1, coordinate[1]))
        if coordinate[0] + 1 <= self.n and coordinate[1] + 1 <= self.n:
            result.append((coordinate[0] + 1, coordinate[1] + 1))

        return [self._encodePoint(point) for point in result]

    def _bfs(self):
        # Check Player 1
        queue = []
        visited = [[False] * (self.n + 1) for i in range(self.n + 1)]
        for i in range(1, self.n + 1):
            if self.board[1][i] == 1:
                queue.append(self._encodePoint((1, i)))
                visited[1][i] = True
        while queue:
            s = queue.pop(0)
            s_temp = self._decodePoint(s)
            s_color = self.board[s_temp[0]][s_temp[1]]
            adj_nodes = self._adjNodes(s)
            for node in adj_nodes:
                temp = self._decodePoint(node)
                if self.board[temp[0]][temp[1]] == s_color and not visited[temp[0]][temp[1]]:
                    queue.append(node)
                    visited[temp[0]][temp[1]] = True
        for i in range(1, self.n + 1):
            if visited[self.n][i]:
                return 1

        # Check Player 2
        queue = []
        visited = [[False] * (self.n + 1) for i in range(self.n + 1)]
        for i in range(1, self.n + 1):
            if self.board[i][1] == 2:
                queue.append(self._encodePoint((i, 1)))
                visited[i][1] = True
        while queue:
            s = queue.pop(0)
            s_temp = self._decodePoint(s)
            s_color = self.board[s_temp[0]][s_temp[1]]
            adj_nodes = self._adjNodes(s)
            for node in adj_nodes:
                temp = self._decodePoint(node)
                if self.board[temp[0]][temp[1]] == s_color and not visited[temp[0]][temp[1]]:
                    queue.append(node)
                    visited[temp[0]][temp[1]] = True
        for i in range(1, self.n + 1):
            if visited[i][self.n]:
                return 2

        return None

    # Update gui and display
    def _updateGui(self):
        self.gui.update(self.board)
        self.gui.display()

    # ----------------------------------------PUBLIC FIELD---------------------------------------------

    # Check either side wins
    # return None if no side wins
    # return 1 if red wins
    # return 2 if blue wins
    def checkWin(self):
        # check use BFS
        return self._bfs()

    # return available moves as a list
    def availableMoves(self):
        moves = []
        for x in range(1, self.n + 1):
            for y in range(1, self.n + 1):
                if not self.board[x][y]:
                    moves.append((x, y))
        return moves

    # Input:(x, y)
    # 1. update board point, make the (x,y) point on the board based on self.round
    # 2. update self.round to the next
    def move(self):
        pass

    # Used to reset the current board for the next round run
    def reset(self):
        pass

    def run(self):
        pass


if __name__ == '__main__':
    pass