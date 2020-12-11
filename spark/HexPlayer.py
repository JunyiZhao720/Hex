class HexPlayer:
    def __init__(self, ai):
        self.ai = ai
        self.index = -1

    def setIndex(self, index):
        self.index = index
        self.ai.setIndex(index)

    def next(self, state):
        return self.ai.solve(self.index, state)





if __name__ == '__main__':
    pass