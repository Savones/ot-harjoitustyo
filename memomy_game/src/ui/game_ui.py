import pygame
HEIGHT = 600
WIDTH = 600

def draw_screen():
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

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    draw_screen()