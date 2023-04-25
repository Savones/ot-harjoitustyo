
class Squares:
    def __init__(self):
        self.square_width = 90
        self.squares = self.set_squares()

    def set_squares(self):
        squares = []
        x_coord = 155
        y_coord = 100
        for i in range(1, 10):
            squares.append((x_coord, y_coord))
            if i % 3 == 0:
                y_coord += 100
                x_coord = 155
            else:
                x_coord += 100
        return squares
