
# Constructor
# A = HexEngine(board=None, human_color_red=False, round=-1, useGui=False)
# A.init(n=3, human_color_red=False, human_move_first=True, gui=HexGui(), ai=HexAI.DDQN(), useGui=True)

class HexEngine:
    # Only for clone use
    def __init__(self, board, human_color_red, round, useGui = False):
        self.board = board
        self.gui = None
        self.round = round          # represents which color to run
        self.useGui = useGui

        # 1 for red, 2 for blue
        if human_color_red:
            self.human_color = 1
            self.AI_color = 2
        else:
            self.human_color = 2
            self.AI_color = 1

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

    # First time run, needs to initialize itself
    def init(self,n, human_color_red, human_move_first, gui, ai, useGui = True):
        self.n = n                                  # size of board
        self.board = self._init_board()             # initialize board
        self.gui = gui
        self.useGui = useGui
        self.ai = ai

        # 1 for red, 2 for blue
        if human_color_red:
            self.human_color = 1
            self.AI_color = 2
        else:
            self.human_color = 2
            self.AI_color = 1

        # if human should go first
        if human_move_first:
            self.round = self.human_color
        else:
            self.round = self.AI_color

    # Check if any side wins
    # return None if no side wins
    # return 1 if red wins
    # return 2 if blue wins
    def wining_check(self):
        pass

    # Next round
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