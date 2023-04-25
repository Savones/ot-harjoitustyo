
class Squares:
    def __init__(self):
        self.square_width = 90
        self.squares = self.set_squares()

    def set_squares(self):
        squares = []
        x = 155
        y = 100
        for i in range(1, 10):
            squares.append((x, y))
            if i % 3 == 0:
                y += 100
                x = 155
            else:
                x += 100
        return squares