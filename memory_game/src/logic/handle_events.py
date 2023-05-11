import pygame
import bcrypt


class LoginEvents:
    """A class that handles events for registration (buttons pressed, mouse movement)

    Attributes:
        check: an object for Check class
        display: an object for RegisDisplay class (login/sign up UI)
        database: an object for the Database class (handles database logic)
        buttons: a list of buttons for registration UI
    """

    def __init__(self, check, display, database, buttons):
        """The classes constructor which initializes the classes variables

        Attributes:
            Listed above
        """

        self.buttons = buttons
        self.check = check
        self.display = display
        self.database = database
        self.input = ""
        self.username = ""

    def reset_input(self):
        """Resets the users input to an empty string
        """

        self.input = ""

    def button_actions(self, pos, event, option, button_number):
        """Checks if a button is clicked
           and handles the click and mouse hovering

        Attributes:
            pos: the mouse cursors position coordinates (x, y)
            event: the current pygame event
            option: int that dictates actions taken when enter pressed
            button_number: tells which button is being checked on the button list

        Returns:
            True if the button is clicked, False if it isn't
        """

        return_value = False
        button = self.buttons[button_number]
        if button.if_hovered(pos):
            self.display.draw_button(True, button)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.name == "CREATE ACCOUNT":
                    self.reset_input()
                    return_value = True
                elif button.name == "ENTER":
                    return_value = self.enter_pressed(option)
                elif button.name == "RETURN":
                    return_value = True
        else:
            self.display.draw_button(False, button)
        return return_value

    def login_username(self, player_input):
        """Checks if the players given username exists

        Attributes:
            player_input: the players username input

        Returns:
            True if the players username exists in the database
            False if it doesn't
        """

        if self.database.player_exists(player_input):
            self.username = player_input
            return True
        print("User not found")
        return False

    def sign_up_username(self, player_input):
        """Checks if username is allowed when player is
           creating a new account

        Attributes:
            player_input: the players username input

        Returns:
            True if the username is allowed, False if it isn't
        """

        if self.database.player_exists(player_input):
            print("Username already in use")
            return False
        if not self.check.valid_username(player_input):
            print("Username has to be 2-6 characters")
            return False

        self.username = player_input
        return True

    def sign_up_password(self, password):
        """Checks if the players created password is allowed
           and if it is, adds the new player to database

        Attributes:
            password: the players password input

        Returns:
            True if the password was accepted and player was added
            False if password not allowed
        """

        if not self.check.valid_password(password):
            print("Password has to have 4-20 characters")
            return False
        password = password.encode()
        hashed_password = self.hash_password(password)
        self.database.add_player(self.username, hashed_password)
        return True

    def hash_password(self, password):
        """Crypts the given password

        Attributes:
            password: the players password input

        Returns:
            The crypted password
        """

        return bcrypt.hashpw(password, bcrypt.gensalt())

    def key_pressed(self, event, option: int):
        """Handles key pressing events

        Attributes:
            event: the current pygame event
            option: tells whether key-press is in log in or sign up display

        Returns:
            True if pressing enter was successfull (entering username/password)
            False in other all cases

        """

        return_value = False
        if event.type != pygame.KEYDOWN:
            return return_value
        if event.key == pygame.K_BACKSPACE:
            self.input = self.input[0: -1]
        elif event.key == pygame.K_RETURN:
            return_value = self.enter_pressed(option)
        else:
            self.input += event.unicode
        self.display.update_screen(self.input, option)
        return return_value

    def enter_pressed(self, option):
        """Handles actions when enter is pressed in log in or sign up display

        Attributes:
            option: tells whether the display is log in or sign up
                    and whether username was already given

        Returns:
            True if the actions were successfull
            False if something went wrong (wrong password etc.)
        """

        if option == 0 and not self.sign_up_password(self.input):
            return False
        if option == -1 and not self.sign_up_username(self.input):
            return False
        if option == 1 and not self.login_username(self.input):
            return False
        if option == 2 and not self.check.if_correct_password(self.username, self.input):
            return False
        return True
