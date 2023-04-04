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
            self.pattern.add_random_press()
            round = self.round()
            if round == None:
                break
            elif round == -1:
                self.display.lost()
                break
        print("done")
    

    def round(self):
        self.display.draw_pattern(self.pattern.pattern_list)
        clicks = 0
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    self.display.draw_click(pos)
                    if not self.check.check_click(pos, self.pattern.pattern_list[clicks]):
                        return -1 
                    clicks += 1
                
                if clicks >= len(self.pattern.pattern_list):
                    return 1

                if event.type == pygame.QUIT:
                    running = False
    