import time
class HexPlayer:
    def __init__(self, ai):
        self.ai = ai
        self.index = -1

    def setIndex(self, index):
        self.index = index

    def next(self, state):
        time_start = time.time()
        result = self.ai.solve(self.index, state)
        print('Player uses ', str(time.time() - time_start), 'seconds.')
        return result





if __name__ == '__main__':
    pass