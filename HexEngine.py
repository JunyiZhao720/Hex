
from HexGui import HexGui
from HexAI import HexAI

import numpy as np
class HexEngine:
    # When constructing the class, use HexEngine.create_new()
    # When need copying, use HexEngine.create_exist()
    # Notice the default constructor should not be used explicitly!!!
    def __init__(self):
        self.n = -1
        self.board = None
        self.gui = None
        self.ai = None
        self.ai_ = None
        self.human_color = -1
        self.AI_color = -1
        self.round = -1
        self.count = 0

    # start from 0
    def _encode_point(self, coordinate):
        return self.n * (coordinate[0] - 1) + coordinate[1] - 1

    # start from (1, 1)
    def _decode_point(self, point):
        if type(point) is tuple:
            return point
        elif type(point) is not int:
            print('_decode error:', type(point))
            return (-1, -1)
        row = point // self.n + 1
        col = point % self.n + 1
        return (row, col)

    def _flip(self, round):
        if round == 2:
            return 1
        else:
            return 2

    def _adj_nodes(self, point):
        result = []
        coordinate = self._decode_point(point)
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

        return [self._encode_point(point) for point in result]


    def _BFS(self):
        # Check Red colors
        queue = []
        visited = [[False] * (self.n + 1) for i in range(self.n + 1)]
        for i in range(1, self.n + 1):
            if self.board[1][i] == 1:
                queue.append(self._encode_point((1, i)))
                visited[1][i] = True
        while queue:
            s = queue.pop(0)
            s_temp = self._decode_point(s)
            s_color = self.board[s_temp[0]][s_temp[1]]
            adj_nodes = self._adj_nodes(s)
            for node in adj_nodes:
                temp = self._decode_point(node)
                if self.board[temp[0]][temp[1]] == s_color and not visited[temp[0]][temp[1]]:
                    queue.append(node)
                    visited[temp[0]][temp[1]] = True
        for i in range(1, self.n + 1):
            if visited[self.n][i]:
                return 1

        # Check Blue colors
        queue = []
        visited = [[False] * (self.n + 1) for i in range(self.n + 1)]
        for i in range(1, self.n + 1):
            if self.board[i][1] == 2:
                queue.append(self._encode_point((i, 1)))
                visited[i][1] = True
        while queue:
            s = queue.pop(0)
            s_temp = self._decode_point(s)
            s_color = self.board[s_temp[0]][s_temp[1]]
            adj_nodes = self._adj_nodes(s)
            for node in adj_nodes:
                temp = self._decode_point(node)
                if self.board[temp[0]][temp[1]] == s_color and not visited[temp[0]][temp[1]]:
                    queue.append(node)
                    visited[temp[0]][temp[1]] = True
        for i in range(1, self.n + 1):
            if visited[i][self.n]:
                return 2

        return None

    # ----------------------------------------PUBLIC FIELD---------------------------------------------
    @staticmethod
    # Generate (n + 1) * (n + 1) sized board
    def init_board(n):
        board = np.zeros((n+1, n+1), dtype=np.int32)
        return board

    @staticmethod
    # Object initialization
    # first time run, needs to initialize itself
    def create_new(n, human_color_red, human_move_first, gui, ai):
        instance = HexEngine()
        instance.n = n                                       # size of board
        instance.board = HexEngine.init_board(n)             # initialize board
        instance.gui = gui
        instance.ai = ai

        # 1 for red, 2 for blue
        if human_color_red:
            instance.human_color = 1
            instance.AI_color = 2
        else:
            instance.human_color = 2
            instance.AI_color = 1

        # if human should go first
        if human_move_first:
            instance.round = instance.human_color
        else:
            instance.round = instance.AI_color
        return instance

    @staticmethod
    # Only for clone use
    def create_exist(board, human_color_red, round, gui, ai):
        instance = HexEngine()
        instance.board = board
        instance.n = len(board) - 1
        instance.round = round          # represents which color to run
        instance.gui = gui
        instance.ai = ai

        # 1 for red, 2 for blue
        if human_color_red:
            instance.human_color = 1
            instance.AI_color = 2
        else:
            instance.human_color = 2
            instance.AI_color = 1
        return instance


    @staticmethod
    # Constructor for only AI to use
    def create_AI_only(n, AI_1_red, AI_1_first, gui, ai):
        instance = HexEngine()
        instance.board = HexEngine.init_board(n)
        instance.n = n
        instance.gui = gui
        instance.ai = ai
        instance.ai_ = ai

        if AI_1_red:
            instance.human_color = 1   #human_color == ai color
            instance.AI_color = 2      #AI_color == ai_ color
        else:
            instance.human_color = 2
            instance.AI_color = 1

        if AI_1_first:
            instance.round = instance.human_color
        else:
            instance.round = instance.AI_color
        return instance

    # Check if any side wins
    # return None if no side wins
    # return 1 if red wins
    # return 2 if blue wins
    def wining_check(self):
        # make sure more than 14 moves are made
        if self.count <= 14:
            return None
        # check use BFS
        return self._BFS()

    # return available moves as a list
    def available_moves(self):
        moves = []
        for x in range(1, self.n + 1):
            for y in range(1, self.n + 1):
                if not self.board[x][y]:
                    moves.append((x, y))
        return moves

    def available_encoded_moves(self):
        return [self._encode_point(point) for point in self.available_moves()]

    # Input:(x, y)
    # 1. update board point, make the (x,y) point on the board based on self.round
    # 2. update self.round to the next
    def move(self, point, useGui=True):
        point = self._decode_point(point)
        row = point[0]
        col = point[1]

        if (self.board[row][col] != 0):
            print('Error: move() used on an occupied plot!')
            return

        if self.round == self.human_color:
            self.board[row][col] = self.human_color
        else:
            self.board[row][col] = self.AI_color

        if useGui:
            self.update_gui()

        self.round = self._flip(self.round)
        self.count += 1

    # Next round
    # call self.move accordingly
    def next(self):
        # TODO: human turn
        if self.round == self.human_color:
            point = self.gui.next_human()
            self.move(point)
        else:
        # TODO: AI turn
            point = self.ai.solve(self)
            self.move(point)

    # Update gui and display
    def update_gui(self):
        self.gui.update(self.board)
        self.gui.display()

    # Clone itself
    # use useGui is False, don't copy gui
    # return HexEngine
    def clone(self, useGui = False, useAI = False):
        board = [row[:] for row in self.board]
        gui = None
        ai = None
        if useGui and self.gui:
            gui = self.gui.clone()
        if useAI and self.ai:
            ai = self.ai.clone()
        return HexEngine.create_exist(board=board,  human_color_red=self.human_color == 1, round=self.round, gui=gui, ai=ai)

    # Used to reset the current board for the next round run
    def reset(self):
        self.board = HexEngine.init_board(self.n)
        self.count = 0


    def run(self):
        while(not self.wining_check()):
            self.next()
        print('Done!')



if __name__ == '__main__':
    # GUI Configuration
    # para = HexGui.configuration_gui()
    para = (8, False, True, True, 'Monte', 'Monte', 1, 2)
    ai = None
    if para[4] == 'Monte':
        ai_color = 1
        if para[2]:
            ai_color = 2
        ai = HexAI.MonteCarlo(AI_color=ai_color)

    engine = HexEngine.create_new(n=para[0], human_color_red=para[2], human_move_first=para[3], gui = HexGui(human_color_red=para[2]), ai=ai)
    #engine.run()
    engine.board = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 2, 2, 2, 2, 2, 2, 2, 1], [0, 2, 1, 2, 2, 1, 2, 2, 1], [0, 1, 1, 2, 2, 1, 1, 1, 2], [0, 1, 2, 2, 2, 2, 1, 1, 1], [0, 1, 1, 2, 1, 2, 2, 1, 1], [0, 1, 1, 1, 1, 1, 2, 2, 2], [0, 2, 2, 2, 1, 2, 1, 1, 1], [0, 1, 1, 2, 2, 2, 1, 1, 1]]
    print(engine.wining_check())
    # engine.run()
    #A = HexEngine.create_new(n=3, human_color_red=True, human_move_first=True, gui=None, ai=None)
