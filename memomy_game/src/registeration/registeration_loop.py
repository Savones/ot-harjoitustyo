import pygame

class RegisterationLoop:
    def __init__(self, database, display, check):
        self.database = database
        self.display = display
        self.check = check
    
    def start(self):

        if self.database.table_exists() == False:
            self.database.create_table()
        
        player_input = ""
        self.display.draw_screen(1)

        running = True

        while running:
            for event in pygame.event.get():
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        player_input = player_input[0: -1]

                    elif event.key == pygame.K_RETURN:

                        if self.database.player_exists(player_input):
                            return player_input

                    else:
                        player_input += event.unicode
                    self.display.update_screen(player_input)
                
                pos = pygame.mouse.get_pos()

                if self.check.if_hovered(pos, 340, 340, 150, 60):
                        self.display.enter_button(True)
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if self.database.player_exists(player_input):
                                return player_input
                else:
                    self.display.enter_button(False)

                if self.check.if_hovered(pos, 170, 490, 260, 55):
                    self.display.create_account_button(True)
                    if event.type == pygame.MOUSEBUTTONDOWN:    
                        self.create_account()
                        player_input = ""
                        self.display.draw_screen(1)
                else:
                    self.display.create_account_button(False)
                    
                if event.type == pygame.QUIT:
                    print("Player closed the game")
                    exit()


    def hit_enter(self, player_input):
        if not self.database.player_exists(player_input):
            self.database.add_player(player_input, 0)
        return True


    def create_account(self):
        self.display.draw_screen(-1)
        username = ""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Player closed the game")
                    exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        username = username[0: -1]

                    elif event.key == pygame.K_RETURN:

                        if self.hit_enter(username):
                            return

                    else:
                        username += event.unicode
                    self.display.update_screen(username)
                
                pos = pygame.mouse.get_pos()

                if self.check.if_hovered(pos, 340, 340, 150, 60):
                        self.display.enter_button(True)
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if self.hit_enter(username):
                                return
                else:
                    self.display.enter_button(False)