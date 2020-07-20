
class HexGui:
    def __init__(self, board, human_color_red):
        self.n = len(board)                                  # size of board
        self.board = board                                   # initialize board

        # 1 for red, 2 for blue
        if human_color_red:
            self.human_color = 1
            self.AI_color = 2
        else:
            self.human_color = 2
            self.AI_color = 1

    # setting GUI
    # receive size n
    # receive if human color is red
    # receive if human move first
    # receive what kind of AI to use
    # receive if only AI plays

    # return n, if_AI_only, human_color_red, human_move_first, AI_type1, AI_type2, AI1_color, AI2_color
    def configuration_gui(self): # for zcx to initialize; AI type; human_move_first, if_AI_only

        n = input("Please set the size: ")
        if_AI_only = input("Only AI, please type True or False: ")
        if_AI_only = if_AI_only.lower()
        # 接受 if_AI_only
        if if_AI_only == 'true':
            # 接受2个AI 输入的字符串
            print("Please type two AI types you want to use")
            AI_type1 = input("First AI type: ")
            AI_type2 = input("Second AI type: ")
        elif if_AI_only == 'false':
            # 接受1个AI
            print("Please only one AI type you want to use")
            if_AI_only = input("AI type: ")
        else:
            print("Invalid input")

        human_color_red = input("Human color is red, please type True or False: ")
        human_color_red = human_color_red.lower()
        if human_color_red != 'true' or 'false':
            print("Invalid input")

        human_move_first = input("Human move first, please type True or False: ")
        human_move_first = human_move_first.lower()
        if human_move_first != 'true' or 'false':
            print("Invalid input")

        AI_type1 = input("Please type DDQN or DQN or Monte Carlo for AI type1: ")
        AI_type1 = AI_type1.lower()
        if AI_type1 != 'DDQN' or 'DQN' or 'Monte Carlo':
            print("Invalid input")

        AI_type2 = input("Please type DDQN or DQN or Monte Carlo for AI type2: ")
        AI_type2 = AI_type2.lower()
        if AI_type2 != 'DDQN' or 'DQN' or 'Monte Carlo':
            print("Invalid input")

        AI1_color = input("Please set the color for AI 1: ")
        AI1_color = AI1_color.lower()
        if AI1_color != 'blue' or 'red':
            print("Invalid input")

        AI2_color = input("Please set the color for AI 2: ")
        AI2_color = AI2_color.lower()
        if AI2_color != 'blue' or 'red':
            print("Invalid input")

        return n, if_AI_only, human_color_red, human_move_first, AI_type1, AI_type2, AI1_color, AI2_color

    # Help function for color name
    def color_name(self):
        if self.human_color == 1:
            print("Human color is 1 or red")
        else:
            print("Human color is 2 or blue")

    # Receive and update the current board
    # 接受一个棋盘，复制copy到本地
    def update(self, board):
        board = board.copy()
        pass

    # Receive (x, y) from human for the next chess move
    # Return (x,y) tuple
    def next_human(self):
        x = input("Please enter x coordinate: ")
        y = input("Please enter y coordinate: ")
        xy_coord = (x,y)
        return xy_coord

    # Display the current state of Hex
    def display(self):
        i = 1
        w = int(input('Please number of rows: '))
        c = int(input('Please number of columns: '))
        while i <= w:
            j = 1
            while j <= i - 1:
                print(" ", end=" ")
                j += 1
            j = 1
            while j <= c:
                print("*", end=" ")
                j += 1
            print()
            i = i + 1

    # Clone the current object
    def clone(self):
        board = [row[:] for row in self.board]
        return HexGui(board=board, human_color_red=self.human_color==1)


if __name__ == '__main__':
    #print('Hello World')
    a = HexGui
    #a.display(a)
    a.configuration_gui(a)


