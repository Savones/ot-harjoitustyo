
class Button:
    def __init__(self, name, x_coord, y_coord, width, height, text_x, text_y, font, colors):
        self.name = name
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.width = width
        self.height = height
        self.text_x = text_x
        self.text_y = text_y
        self.font = font
        self.colors = colors

    def if_hovered(self, pos):
        if (self.x_coord + self.width) >= pos[0] >= self.x_coord and (self.y_coord + self.height) >= pos[1] >= self.y_coord:
            return True
        return False
