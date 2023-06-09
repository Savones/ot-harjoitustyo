import sys
import pygame

from logic.handle_events import LoginEvents


class RegisterationLoop:
    """A class that runs the game before logging in

    Attributes:
        database: an object for the Database class (handles database logic)
        display: an object for RegisDisplay class (registration UI)
        check: an object for Check class
        buttons: a list of buttons for differents UI views
    """

    def __init__(self, database, display, check, buttons):
        """The classes constructor which initializes the classes variables

        Args:
            Listed above
        """

        self.login_buttons = buttons[0]
        self.sign_up_buttons = buttons[1]
        self.database = database
        self.display = display
        self.events = LoginEvents(check, display, database, buttons)
        self.name_entered = False
        self.running = True

    def start_log_in(self):
        """Handles the pygame events in the log-in display

        Returns:
            The players username once logging in has been successfull
        """

        if self.database.table_exists() is False:
            self.database.create_table()

        self.display.draw_screen(1)

        while self.running:
            for event in pygame.event.get():

                if not self.name_entered and self.events.key_pressed(event, 1):
                    self.username_entered(1)

                elif self.name_entered and self.events.key_pressed(event, 2):
                    return self.events.username

                pos = pygame.mouse.get_pos()

                if not self.name_entered and self.events.button_actions(pos, event, 1, 0):
                    self.username_entered(1)

                elif self.name_entered and self.events.button_actions(pos, event, 2, 0):
                    return self.events.username

                if self.events.button_actions(pos, event, 0, 1):
                    self.create_account()
                    self.events.reset_input()
                    self.name_entered = False
                    self.display.draw_screen(1)

                if event.type == pygame.QUIT:
                    print("Player closed the game")
                    sys.exit()
        return None

    def create_account(self):
        """Handles the pygame events in the sign-up display

        Returns:
            None once an account was created
        """

        self.display.draw_screen(-1)
        self.name_entered = False

        while self.running:
            for event in pygame.event.get():

                if not self.name_entered and self.events.key_pressed(event, -1):
                    self.username_entered(-1)

                elif self.name_entered and self.events.key_pressed(event, 0):
                    print("New account created")
                    return None

                pos = pygame.mouse.get_pos()

                if not self.name_entered and self.events.button_actions(pos, event, -1, 0):
                    self.username_entered(-1)

                elif self.name_entered and self.events.button_actions(pos, event, 0, 0):
                    print("New account created")
                    return None

                if not self.name_entered and self.events.button_actions(pos, event, 0, 2):
                    return None

                if self.name_entered and self.events.button_actions(pos, event, 0, 2):
                    self.name_entered = False
                    self.display.draw_screen(-1)

                if event.type == pygame.QUIT:
                    sys.exit()
        return None

    def username_entered(self, option):
        """Changes to password view once username has been entered

        Args:
            option: tells whether the password view is for log-in or sign-up

        Returns:
            None
        """

        self.name_entered = True
        self.events.reset_input()
        self.display.password_display(option)
