
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

        self.r = 1
        self.b = 2

    def reverse(self):
        res = [[0] * (self.n + 1)]

        j = self.n
        while j >= 1:
            tem = [0]
            i = self.n
            while i >= 1:
                tem.append(self.board[i][j])
                i -= 1
            j -= 1
            res.append(tem)
        self.board = res

    # Two algorithms but only choose one
    def _BFS(self, red):
        target = 0
        if red:
            target = self.r
        else:
            target = self.b
        stack = []
        copy = [row[1:] for row in self.board[1:]]
        length = len(copy) - 1
        for i in range(length + 1):
            if (copy[0][i] == target):
                stack.insert(0, [0, i])
        if (len(stack) == 0):
            return False

        while len(stack) != 0:
            node = stack.pop(0)
            row = node[0]
            col = node[1]
            copy[row][col] = -1

            if row == length:
                return True
            if row + 1 <= length:
                if copy[row + 1][col] == target:
                    stack.insert(0, [row + 1, col])
                if col - 1 >= 0 and copy[row + 1][col - 1] == target:
                    stack.insert(0, [row + 1, col - 1])
            if row - 1 >= 0:
                if copy[row - 1][col] == target:
                    stack.insert(0, [row - 1, col])
                if col + 1 <= length and copy[row - 1][col + 1] == target:
                    stack.insert(0, [row - 1, col + 1])
            if col - 1 >= 0:
                if copy[row][col - 1] == target:
                    stack.insert(0, [row, col - 1])
            if col + 1 <= length:
                if copy[row][col + 1] == target:
                    stack.insert(0, [row, col + 1])

    def _decode_point(self, point):
        point_local = point
        if type(point_local).__module__ == np.__name__ or type(point_local) == int:
            if np.size(point_local) == 1:
                row = point_local // (self.n + 1) + 1
                col = point_local % self.n
                if col == 0:
                    col = self.n
                return (row, col)
        elif len(point_local) == 2:
            return point_local

        print('_decode error:', point_local)
        return (0, 0)

    def _encode_point(self, point):
        return self.n * (point[0] - 1) + point[1]

    def _flip(self, round):
        if round == 2:
            return 1
        else:
            return 2

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
        instance.n = n                                      # size of board
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
    # TODO: write a constructor that only accepts AI as players
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
        red = self._BFS(True)
        self.reverse()
        blue = self._BFS(False)
        self.reverse()
        if red:
            return 1
        elif blue:
            return 2
        else:
            return None

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
        # TODO
        point = self._decode_point(point)
        row = point[0]
        col = point[1]

        if (self.board[row][col] != 0):
            print('Error: move() used on an occupied plot!')

        if self.round == self.human_color:
            self.board[row][col] = self.human_color
        else:
            self.board[row][col] = self.AI_color

        if useGui:
            self.update_gui()
        self.round = self._flip(self.round)

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
    #engine.board = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 2, 2, 2, 2, 2, 2, 2, 1], [0, 2, 1, 2, 2, 1, 2, 2, 1], [0, 1, 1, 2, 2, 1, 1, 1, 2], [0, 1, 2, 2, 2, 2, 1, 1, 1], [0, 1, 1, 2, 1, 2, 2, 1, 1], [0, 1, 1, 1, 1, 1, 2, 2, 2], [0, 2, 2, 2, 1, 2, 1, 1, 1], [0, 1, 1, 2, 2, 2, 1, 1, 1]]
    #print(engine.wining_check())
    engine.run()
    #A = HexEngine.create_new(n=3, human_color_red=True, human_move_first=True, gui=None, ai=None)
