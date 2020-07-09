


class HexEngine:
    # When constructing the class, use HexEngine.create_new()
    # When need copying, use HexEngine.create_exist()
    # Notice the default constructor should not be used explicitly!!!
    def __init__(self):
        self.n = -1
        self.board = None
        self.gui = None
        self.useGui = False
        self.ai = None
        self.human_color = -1
        self.AI_color = -1
        self.round = -1

    # Generate (n + 1) * (n + 1) sized board
    def _init_board(self):
        board = []
        for i in range(self.n + 1):
            board.append([0] * (self.n + 1))
        return board

    # Two algorithms but only choose one
    def _BFS(self):
        pass
    def _DFS(self):
        pass

    # ----------------------------------------PUBLIC FIELD---------------------------------------------

    @staticmethod
    # Object initialization
    # first time run, needs to initialize itself
    def create_new(n, human_color_red, human_move_first, gui, ai, useGui = True):
        instance = HexEngine()
        instance.n = n                                      # size of board
        instance.board = instance._init_board()             # initialize board
        instance.gui = gui
        instance.useGui = useGui
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
    def create_exist(board, human_color_red, round, useGui = False):
        instance = HexEngine()
        instance.board = board
        instance.gui = None
        instance.round = round          # represents which color to run
        instance.useGui = useGui

        # 1 for red, 2 for blue
        if human_color_red:
            instance.human_color = 1
            instance.AI_color = 2
        else:
            instance.human_color = 2
            instance.AI_color = 1
        return instance

    # Check if any side wins
    # return None if no side wins
    # return 1 if red wins
    # return 2 if blue wins
    def wining_check(self):
        pass

    # return available moves as a list
    def available_moves(self):
        moves = []
        for x in range(1, self.n + 1):
            for y in range(1, self.n + 1):
                if not self.board[x][y]:
                    moves.append((x, y))
        return moves

    # Input:(x, y)
    # 1. update board point, make the (x,y) point on the board based on self.round
    # 2. update self.round to the next
    def move(self, point):
        pass

    # Next round
    # call self.move accordingly
    def next(self):
        # TODO: human turn
        if self.round == self.human_color:
            pass
        else:
        # TODO: AI turn
            pass

    # Update gui and display
    def update_gui(self):
        pass

    # Clone itself
    # use useGui is False, don't copy gui
    # return HexEngine
    def clone(self, useGui=False):
        pass

if __name__ == '__main__':
    print('Hello World')
    A = HexEngine.create_new(n=3, human_color_red=True, human_move_first=True, gui=None, ai=None, useGui = True)