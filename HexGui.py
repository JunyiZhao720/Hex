


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

    # ----------------------------------------PUBLIC FIELD---------------------------------------------

    @staticmethod
    # For the overall board setting GUI
    # receive size n
    # receive if human color is red
    # receive if human move first
    # receive what kind of AI to use
    def configuration_gui():
        pass

    # Help function for color name
    def color_name(self):
        if self.human_color == 1:
            print("Human color is 1 or red")
        else:
            print("Human color is 2 or blue")

    # Receive and update the current board
    def update(self, board):
        pass

    # Receive (x, y) from human for the next chess move
    def next_human(self):
        pass

    # Display the current state of Hex
    def display(self):
        pass


if __name__ == '__main__':
    print('Hello World')