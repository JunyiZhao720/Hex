# from HexEngine import HexEngine

class HexGui:
    red = "\033[31m"
    blue = "\033[36m"
    default = '\033[39m'

    @staticmethod
    def _coloredStar(index):
        if index == 1:
            return HexGui.red + '*' + HexGui.default
        if index == 2:
            return HexGui.blue + '*' + HexGui.default
        return '*'


    # Display the current state of Hex
    @staticmethod
    def display(state):
        n = len(state) - 1

        for i in range(1, n + 1):
            for k in range(i):
                print('  ', end='')
            # print stars
            print(HexGui._coloredStar(state[i][1]), end='')
            for j in range(2, n + 1):
                print('   ' + HexGui._coloredStar(state[i][j]), end='')
            print()



if __name__ == '__main__':
    pass
    # state = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 2, 1, 2, 2, 2, 2, 1, 1], [0, 1, 2, 1, 2, 1, 2, 1, 2], [0, 1, 2, 1, 2, 2, 2, 1, 1], [0, 2, 1, 1, 2, 2, 1, 1, 1], [0, 1, 1, 2, 1, 2, 2, 1, 1], [0, 1, 2, 2, 2, 1, 2, 2, 1], [0, 1, 1, 2, 1, 2, 2, 1, 2], [0, 1, 1, 1, 1, 2, 2, 2, 2]]
    # state = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 2, 2, 2, 2, 2, 2, 2, 1], [0, 2, 1, 2, 2, 1, 2, 2, 1], [0, 1, 1, 2, 2, 1, 1, 1, 2], [0, 1, 2, 2, 2, 2, 1, 1, 1], [0, 1, 1, 2, 1, 2, 2, 1, 1], [0, 1, 1, 1, 1, 1, 2, 2, 2], [0, 2, 2, 2, 1, 2, 1, 1, 1], [0, 1, 1, 2, 2, 2, 1, 1, 1]]
    state = [
        [0, 0, 0, 0],
          [0, 0, 2, 2],
            [0, 2, 0, 0],
              [2, 0, 0, 0]
    ]
    HexGui.display(state)



