
class Button:
    """A class that initializes a button

    Attributes:
        name: The text on the button
        x_coord: The buttons left x-coordinate
        y_coord: The buttons top y-coordinate
        width: The buttons width
        height: The buttons height
        text_x: The texts left x-coordinate
        text_y: The texts top y-coordinate
        font: The texts font-size
        colors: The buttons two colors
    """

    def __init__(self, name, box_coordinates, text_x, text_y, font, colors):
        """The classes constructor which creates a button

        Args:
            Listed above
        """

        self.name = name
        self.x_coord = box_coordinates[0]
        self.y_coord = box_coordinates[1]
        self.width = box_coordinates[2]
        self.height = box_coordinates[3]
        self.text_x = text_x
        self.text_y = text_y
        self.font = font
        self.colors = colors
        self.pressed = False

    def if_hovered(self, pos):
        """Checks if mouse is hovering a button

        Args:
            pos: users mouse position (x, y)

        Returns:
            True if button is hovered, else returns False
        """

        if self.x_coord + self.width >= pos[0] >= self.x_coord:
            if self.y_coord + self.height >= pos[1] >= self.y_coord:
                return True
        return False
