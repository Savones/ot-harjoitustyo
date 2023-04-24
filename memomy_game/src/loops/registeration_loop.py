import sys
import pygame

from logic.handle_events import LoginEvents

class RegisterationLoop:
    def __init__(self, database, display, check):
        self.database = database
        self.display = display
        self.events = LoginEvents(check, display, database)

    def start(self):

        if self.database.table_exists() is False:
            self.database.create_table()

        self.display.draw_screen(1)
        name_entered = False
        running = True

        while running:
            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    if not name_entered and self.events.key_pressed(event, 1):
                        name_entered = True
                        self.events.reset_input()
                        self.display.password_display(1)
                    
                    elif name_entered and self.events.key_pressed(event, 2):
                        return self.events.get_username()

                pos = pygame.mouse.get_pos()

                if not name_entered and self.events.login_enter(pos, event, 1):
                    name_entered = True
                    self.events.reset_input()
                    self.display.password_display(1)
                
                elif name_entered and self.events.login_enter(pos, event, 2):
                    return self.events.get_username()
                
                if self.events.login_create_account(pos, event):
                    self.create_account()
                    self.events.reset_input()
                    name_entered = False
                    self.display.draw_screen(1)

                if event.type == pygame.QUIT:
                    print("Player closed the game")
                    sys.exit()
        return None

    def create_account(self):

        self.display.draw_screen(-1)
        name_entered = False
        running = True

        while running:
            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    if not name_entered and self.events.key_pressed(event, -1):
                        name_entered = True
                        self.events.reset_input()
                        self.display.password_display(-1)
                
                    elif name_entered and self.events.key_pressed(event, 0):
                        print("New account created")
                        return None

                pos = pygame.mouse.get_pos()

                if not name_entered and self.events.enter_button(pos, event, -1):
                    name_entered = True
                    self.events.reset_input()
                    self.display.password_display(-1)
                
                elif name_entered and self.events.enter_button(pos, event, 0):
                    print("New account created")
                    return None
                
                if not name_entered and self.events.return_button(pos, event):
                    return None
                
                elif name_entered and self.events.return_button(pos, event):
                    name_entered = False
                    self.display.draw_screen(-1)

                if event.type == pygame.QUIT:
                    sys.exit()
        return None