class Human:

    def solve(self, index, state):
        x = int(input("Please enter x coordinate: "))
        y = int(input("Please enter y coordinate: "))
        n = len(state) - 1

        while x < 1 or x > n or y < 1 or y > n:
            print("Bad input, please input between [1," + str(n) + "]")
            x = int(input("Please enter x coordinate: "))
            y = int(input("Please enter y coordinate: "))
        return (x, y)