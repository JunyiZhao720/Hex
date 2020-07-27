class H:
    # When constructing the class, use HexEngine.create_new()
    # When need copying, use HexEngine.create_exist()
    # Notice the default constructor should not be used explicitly!!!
    def __init__(self):
        self.n = -1
        self.board = None
        self.gui = None
        self.ai = None
        self.human_color = -1
        self.AI_color = -1
        self.round = -1

        self.r = 1
        self.b = 2

    def reverse(self):
        res = [[None]]

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

    def BFS(self, red):
        target = 0
        if red:
            target = self.r
        else:
            target = self.b
        stack = []
        copy = [row[1:] for row in self.board[1:]]
        length = len(copy) - 1
        for i in range(length + 1):
            if(copy[0][i] == target):
                stack.insert(0, [0, i])
        if(len(stack) == 0):
            return False

        while len(stack) != 0:
            node = stack.pop(0)
            row = node[0]
            col = node[1]
            copy[row][col] = -1

            if row == length:
                return True
            if row + 1 <= length:
                if copy[row+1][col] == target:
                    stack.insert(0, [row+1, col])
                if col - 1 >= 0 and copy[row+1][col-1] == target:
                    stack.insert(0, [row + 1, col - 1])
            if row - 1 >= 0:
                if copy[row-1][col] == target:
                    stack.insert(0, [row-1, col])
                if col + 1 <= length and copy[row -1][col+1] == target:
                    stack.insert(0, [row - 1, col+1])
            if col - 1 >= 0:
                if copy[row][col-1] == target:
                    stack.insert(0, [row, col-1])
            if col + 1 <= length:
                if copy[row][col+1] == target:
                    stack.insert(0, [row, col+1])

    def wining_check(self):
        print(self.board)
        red = self.BFS(True)
        self.reverse()
        print(self.board)
        blue = self.BFS(False)
        if red:
            return 1
        elif blue:
            return 2
        else:
            return None

    @staticmethod
    # Generate (n + 1) * (n + 1) sized board
    def init_board(n):
        board = []
        for i in range(n + 1):
            board.append([0] * (n + 1))
        return board

    @staticmethod
    # Only for clone use
    def create_exist(board, human_color_red, round, gui, ai):
        instance = H()
        instance.board = board
        instance.n = len(board) - 1
        instance.round = round  # represents which color to run
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

    def create_new(n, human_color_red, human_move_first, gui, ai):
        instance = H()
        instance.n = n  # size of board
        instance.board = H.init_board(n)  # initialize board
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



# h = H().create_new(4, 1, True, None, 1)
# res = [[1,0,1,1],[1,1,0,1],[0,0,1,0],[0,0,1,0]]
#res = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 2, 1, 2, 2, 2, 2, 1, 1], [0, 1, 2, 1, 2, 1, 2, 1, 2], [0, 1, 2, 1, 2, 2, 2, 1, 1], [0, 2, 1, 1, 2, 2, 1, 1, 1], [0, 1, 1, 2, 1, 2, 2, 1, 1], [0, 1, 2, 2, 2, 1, 2, 2, 1], [0, 1, 1, 2, 1, 2, 2, 1, 2], [0, 1, 1, 1, 1, 2, 2, 2, 2]]
# res =[
#         [0, 0, 0, 0, 0],
#           [0, 0, 1, 2, 0],
#             [0, 2, 1, 2, 2],
#               [0, 1, 0, 0, 0],
#                 [0, 1, 0, 0, 0]
#
#     ]
# res = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 2, 1, 1, 2, 1, 2, 1, 1], [0, 2, 1, 1, 2, 2, 2, 1, 1], [0, 1, 2, 1, 2, 1, 1, 2, 1], [0, 2, 2, 1, 1, 2, 2, 1, 1], [0, 1, 1, 2, 1, 1, 2, 2, 2], [0, 2, 1, 2, 1, 1, 1, 2, 1], [0, 2, 1, 2, 2, 2, 2, 1, 1], [0, 2, 2, 2, 2, 1, 2, 1, 2]]
res = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 2, 1, 2, 1, 2, 1, 1, 1], [0, 2, 2, 2, 1, 2, 1, 2, 2], [0, 2, 1, 1, 1, 2, 1, 2, 1], [0, 2, 1, 1, 2, 2, 1, 2, 1], [0, 1, 1, 1, 1, 1, 2, 2, 2], [0, 1, 2, 2, 2, 1, 2, 2, 2], [0, 2, 2, 1, 2, 1, 2, 1, 1], [0, 1, 2, 1, 2, 2, 1, 1, 1]]
# res = [[0,1,0,0],[0,1,1,1],[0,0,0,1],[0,1,1,0]]
h = H().create_exist(res, 1, 1, None, None)
# t = h.BFS(False)
t = h.wining_check()
print(t)

# def BFS(m, red):
#     target = 0
#     if red:
#         target = 1
#     else:
#         target = 2
#     stack = []
#     copy = m.copy()
#     length = len(m)-1
#     for i in range(length + 1):
#         if(copy[0][i] == target):
#             stack.insert(0, [0, i])
#             break
#     if(len(stack) == 0):
#         return False
#
#     while len(stack) != 0:
#         node = stack.pop(0)
#         row = node[0]
#         col = node[1]
#         copy[row][col] = -1
#
#         if row == length:
#             return True
#         if row + 1 <= length:
#             if copy[row+1][col] == target:
#                 stack.insert(0, [row+1, col])
#             if col - 1 >= 0 and copy[row+1][col-1] == target:
#                 stack.insert(0, [row + 1, col - 1])
#         if row - 1 >= 0:
#             if copy[row-1][col] == target:
#                 stack.insert(0, [row-1, col])
#             if col + 1 <= length and copy[row -1][col+1] == target:
#                 stack.insert(0, [row - 1, col+1])
#         if col - 1 >= 0:
#             if copy[row][col-1] == target:
#                 stack.insert(0, [row, col-1])
#         if col + 1 <= length:
#             if copy[row][col+1] == target:
#                 stack.insert(0, [row, col+1])
#
# res = [[0,1,0,0],[0,1,1,1],[0,0,0,1],[0,1,1,0]]
# g = BFS(res, 1)
# print(g)