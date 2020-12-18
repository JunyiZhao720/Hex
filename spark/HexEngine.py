
from spark.HexGui import HexGui
from spark.HexPlayer import HexPlayer
from spark.model.BFS import BFS

import numpy as np
class HexEngine:
    # When constructing the class, use HexEngine.create_new()
    # When need copying, use HexEngine.create_exist()
    # Notice the default constructor should not be used explicitly!!!
    def __init__(self, n, player1, player2, gui, player1First = True):
        self.n = n
        self.players = {}
        player1.setIndex(1)
        player2.setIndex(2)
        self.players[1] = player1
        self.players[2] = player2
        self.gui = gui
        self.player1First = player1First
        self.reset()


    # ----------------------------------------PUBLIC FIELD---------------------------------------------

    # Used to reset the current state for the next round run
    def reset(self):
        self.state = np.zeros((self.n+1, self.n+1), dtype=np.int32)
        if self.player1First:
            self.round = self.players[1]
        else:
            self.round = self.players[2]

    # check either side wins
    # return None if no side wins
    # return 1 or 2 if the associated player wins
    def checkWin(self):
        # check use BFS
        return BFS.bfs(self.state)

    # return available moves as a list
    def availableMoves(self):
        moves = []
        for x in range(1, self.n + 1):
            for y in range(1, self.n + 1):
                if not self.state[x][y]:
                    moves.append((x, y))
        return moves
    # Update gui and display
    def updateGui(self):
        self.gui.display(self.state)

    # 1. update state point, make the (x,y) point on the state based on self.round
    # 2. update self.round to the next
    def next(self):
        move = self.round.next(self.state)

        if self.round == self.players[1]:
            self.state[move[0]][move[1]] = 1
            self.round = self.players[2]
        else:
            self.state[move[0]][move[1]] = 2
            self.round = self.players[1]

    def run(self):
        self.updateGui()
        won = None

        while won is None:
            self.next()
            self.updateGui()
            won = self.checkWin()
        print('player ', won, ' wins!')

from spark.model.Human import Human
from spark.model.MonteCarlo import MonteCarlo

if __name__ == '__main__':
    p2 = HexPlayer(ai = Human())
    p1 = HexPlayer(ai = MonteCarlo(n_copies=1000))
    engine = HexEngine(n=8, player1=p1, player2=p2, gui=HexGui)
    engine.run()
