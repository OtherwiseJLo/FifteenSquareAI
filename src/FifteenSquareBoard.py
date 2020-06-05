import numpy as np


class Square:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def define_neighbors(self):
        pass

    def __repr__(self):
        return self.value


class FifteenSquareBoard:
    def __init__(self):
        squares = [Square(i) for i in range(1, 16)] + ['']
        self.board = np.array(squares).reshape([4,4])
