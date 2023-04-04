import pygame

class Loop:

    def __init__(self, pattern, check, display):
        self.pattern = pattern
        self.check = check
        self.display = display


    def start(self):
        pygame.init()
        self.display.draw_screen()
        while True: 
            self.pattern.level_up()
            self.pattern.add_random_press()
            round = self.round()
            if round == None:
                break
            elif round == -1:
                self.display.lost()
                break
    

    def round(self):
        self.display.draw_pattern(self.pattern.pattern_list, self.pattern.level)
        clicks = 0
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if not self.check.check_misclick(pos):
                        continue
                    elif not self.check.check_click(pos, self.pattern.pattern_list[clicks]):
                        self.display.draw_click(pos)
                        return -1 
                    else:
                        self.display.draw_click(pos)
                        clicks += 1
                
                if clicks >= len(self.pattern.pattern_list):
                    return 1

                if event.type == pygame.QUIT:
                    running = False
    