import pygame

class Loop:

    def __init__(self, pattern, check, display, game_over_display):
        self.pattern = pattern
        self.check = check
        self.display = display
        self.game_over_display = game_over_display
        pygame.init()
        

    def start(self):
        self.display.draw_screen()
        self.pattern.default()
        while True: 
            self.pattern.level_up()
            self.pattern.add_random_press()
            round = self.round()
            if round == None:
                break
            elif round == -1:
                self.game_over()
                break
    

    def round(self):
        self.display.draw_pattern(self.pattern.pattern_list, self.pattern.level)
        clicks = 0
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()

                    # continues if player doesn't hit a square
                    if not self.check.check_misclick(pos):
                        continue

                    # once player hits the squere, returns -1 if wrong answer
                    elif not self.check.check_click(pos, self.pattern.pattern_list[clicks]):
                        self.display.draw_click(pos)
                        return -1 

                    # continues if hits the correct square
                    else:
                        self.display.draw_click(pos)
                        clicks += 1
                
                # goes to next level once player complites pattern without fail
                if clicks >= len(self.pattern.pattern_list):
                    return 1

                if event.type == pygame.QUIT:
                    print("Player closed the game")
                    running = False
    

    def game_over(self):
        self.game_over_display.draw_screen()
        running = True
        while running:
            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()

                    # if "try again" box is clicked -> starts game again
                    if self.check.check_try_again(pos):
                        self.game_over_display.try_again_hover()
                        self.start()

                if event.type == pygame.QUIT:
                        print("Player closed the game")
                        running = False