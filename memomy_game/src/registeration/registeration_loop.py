import pygame

class RegisterationLoop:
    def __init__(self, database, display, check):
        self.database = database
        self.display = display
        self.check = check
    
    def start(self):

        player_input = ""

        if self.database.table_exists() == False:
            self.database.create_table()

        self.display.draw_screen()
        running = True

        while running:
            for event in pygame.event.get():
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        player_input = player_input[0: -1]

                    elif event.key == pygame.K_RETURN:

                        if not self.database.player_exists(player_input):
                            self.database.add_player(player_input, 0)

                        if self.check.check_if_valid(player_input):
                            return player_input
                        
                        self.display.username_unvalid()

                    else:
                        player_input += event.unicode
                    self.display.update_screen(player_input)
                
                pos = pygame.mouse.get_pos()

                if self.check.if_hovered(pos, 340, 340, 150, 60):
                        self.display.enter_button(True)
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if self.check.check_if_valid(player_input):
                                return player_input
                        
                            self.display.username_unvalid()
                else:
                    self.display.enter_button(False)
                
                
                if event.type == pygame.QUIT:
                    print("Player closed the game")
                    exit()

        

