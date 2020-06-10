import numpy as np
from itertools import product


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
        self.valid_board_indices = set(product(range(4), range(4)))
        self.board = np.array(squares).reshape([4, 4])
        self.empty_square = self.board[3][3]
        self.empty_square_idx = self.find_emtpy_square()

        self.adjacent_square_indices = set(
            idx for idx in product(range(-1, 2), range(-1, 2)) if abs(sum(idx)) == 1
        )
        self.candidate_squares = self._find_candidate_squares()

    def _shuffle(self):
        pass

    def find_emtpy_square(self):
        return tuple(idx[0] for idx in np.where(self.board == self.empty_square))

    def _find_candidate_squares(self):
        candidates = set(
            (self.empty_square_idx[0] + a, self.empty_square_idx[1] + b)
            for a, b in self.adjacent_square_indices
        )
        return candidates & self.valid_board_indices

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
