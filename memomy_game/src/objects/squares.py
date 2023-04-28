
class Squares:
    """A class that initializes the list of squares for the game
    """

    def __init__(self):
        """The classes constructor which creates the list of squares
        """

        self.square_width = 90
        self.squares = self.set_squares()

    def set_squares(self):
        """Creates a list of 9 coordinates, each coordinate is a squares top-left corner

        Returns:
            The list of the squares coordinates
        """

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
