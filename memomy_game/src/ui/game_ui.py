import pygame
HEIGHT = 600
WIDTH = 600

class Display:
    def draw_screen(self):
        pygame.init()
        display = pygame.display.set_mode((WIDTH, HEIGHT))
        square_color = (255, 255, 255)

        x = 155
        y = 100
        for i in range(1, 10):
            pygame.draw.rect(display, square_color, pygame.Rect(x, y, 90, 90))
            if i % 3 == 0:
                y += 100
                x = 155
            else:
                x += 100

        pygame.display.flip()

    def draw_click(self, pos):
        display = pygame.display.set_mode((WIDTH, HEIGHT))
        square_color = (255, 255, 255)

        x = 155
        y = 100
        for i in range(1, 10):
            if (x + 90) >= pos[0] >= x and (y + 90) >= pos[1] >= y:
                pygame.draw.rect(display, (200, 0, 0), pygame.Rect(x, y, 90, 90))
            else:
                pygame.draw.rect(display, square_color, pygame.Rect(x, y, 90, 90))
            if i % 3 == 0:
                y += 100
                x = 155
            else:
                x += 100
        
        pygame.display.flip()
        pygame.time.delay(100)
        self.draw_screen()


    def draw_pattern(self, pattern):
        print(pattern)
