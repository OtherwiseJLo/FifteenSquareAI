import numpy as np


class Square:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def define_neighbors(self):
        pass

    def __repr__(self):
        return str(self.value).rjust(2, " ")

    def __str__(self):
        return str(self.value)


class FifteenSquareBoard:
    def __init__(self):
        squares = [Square(i) for i in range(1, 16)]
        squares.append(Square(" "))
        assert len(squares) == 16
        self.board = np.array(squares).reshape([4, 4])
        self.empty_square = self.board[3][3]

    def _shuffle(self):
        pass

    def find_emtpy_square(self):
        return np.where(self.board == self.empty_square)

    def __repr__(self):
        divider = "+---+---+---+---+"
        result = []
        result.append(divider)
        for i in range(4):
            result.append("| {} | {} | {} | {} |".format(*self.board[i, :]))
            result.append(divider)
        return "\n".join(result)


if __name__ == "__main__":
    test = FifteenSquareBoard()
