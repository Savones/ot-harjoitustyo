import pygame
HEIGHT = 500
WIDTH = 500

def draw_screen():
    pygame.init()
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    square_color = (255, 255, 255)

    x = 135
    y = 75
    for i in range(1, 10):
        pygame.draw.rect(display, square_color, pygame.Rect(x, y, 70, 70))
        if i % 3 == 0:
            y += 80
            x = 135
        else:
            x += 80

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    draw_screen()