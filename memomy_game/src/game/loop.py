import pygame

class Loop:

    def __init__(self, pattern, show_pattern, check, display):
        self.pattern = pattern
        self.show_pattern = show_pattern
        self.check = check
        self.display = display

    def start_text_based_version(self):

        # breaks when player fails, every new loop is new level
        while True:
            over = False
            self.pattern.add_random_press()
            # rn is a text ui, should become graphic ui
            self.show_pattern.show_pattern(self.pattern.pattern_list)

            # breaks when player fails or gets to next level by getting the pattern correct
            for i in range(len(self.pattern.pattern_list)):
                # rn player input is text and not clicking on graphic ui      
                player_input_row = int(input(f"{i + 1}. row: "))
                player_input_column = int(input(f"{i + 1}. column: "))
                player_input = [player_input_row, player_input_column]
                bool = self.check.check_player_input(player_input, self.pattern.pattern_list[i])

                if bool == False:
                    print("Game over")
                    over = True
                    break

            if over:
                break
    
    # here would start the actual program
    def start(self):
        self.display.draw_screen()
        while True: 
            self.pattern.add_random_press()
            if self.round() != 1:
                break
        print("done")
    

    def round(self):
        self.display.draw_pattern(self.pattern.pattern_list)

        clicks = 0
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicks += 1
                    pos = pygame.mouse.get_pos()
                    self.display.draw_click(pos)
                
                if clicks >= len(self.pattern.pattern_list):
                    return 1

                if event.type == pygame.QUIT:
                    running = False
    
    def check_pos(self, pos):
        pass