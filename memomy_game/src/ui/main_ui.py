import pygame


class MainUi():
    def __init__(self, display):
        self.display = display
        pygame.init()

    def draw_box(self, color, x, y, width, height):
        pygame.draw.rect(self.display, color, pygame.Rect(
            x, y, width, height), 0, 15)

    def draw_text(self, color, x, y, font_size, content):
        font = pygame.font.SysFont("Inter", font_size)
        text = font.render(content, True, color)
        self.display.blit(text, (x, y))

    def draw_button(self, hovered: bool, button):
        if not hovered:
            text_color = button.colors[0]
            box_color = button.colors[1]
        else:
            text_color = button.colors[1]
            box_color = button.colors[0]

        self.draw_box(box_color, button.x_coord, button.y_coord, button.width, button.height)
        self.draw_text(text_color, button.text_x, button.text_y, button.font, button.name)