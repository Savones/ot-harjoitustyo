import bcrypt


class Check:
    """A class that checks if statements are correct

    Attributes:
        database: an object for the class Database
        squares: the list of squares coordinates for the game
    """

    def __init__(self, database, squares):
        """The classes constructor

        Args:
            Listed above
        """

        self.database = database
        self.squares = squares.squares
        self.square_width = squares.square_width

    def check_click(self, pos, correct_answer):
        """Checks if the player clicked the correct square

        Args:
            pos: the players clicks coordinates (x, y)
            correct_answer: which square should be clicked (numbered 0-8)
        
        Returns:
            True if players click is inside the correct squares area, otherwise False
        """

        correct_x = self.squares[correct_answer][0]
        correct_y = self.squares[correct_answer][1]

        if (correct_x + self.square_width) >= pos[0] >= correct_x:
            if (correct_y + self.square_width) >= pos[1] >= correct_y:
                return True
        return False

    def check_misclick(self, pos):
        """Checks if player hit any square

        Args:
            pos: the players clicks coordinates (x, y)
        
        Returns:
            True if players clicked inside one of the squares area, otherwise False
        """

        for square in self.squares:
            if (square[0] + self.square_width) >= pos[0] >= square[0]:
                if (square[1] + self.square_width) >= pos[1] >= square[1]:
                    return True
        return False

    def valid_username(self, username):
        """Checks if the user entered a valid username when signing up

        Args:
            username: users input when creating an account
        
        Returns:
            True if username is valid, otherwise False
        """

        if len(username) >= 7 or len(username) <= 1:
            return False
        return True

    def valid_password(self, password):
        """Checks if the user entered a valid password when signing up

        Args:
            password: users input when creating an account and username already entered
        
        Returns:
            True if password is valid, otherwise False
        """

        if len(password) > 20 or len(password) < 4:
            return False
        return True

    def if_hovered(self, pos, x_coord, y_coord, width, height):
        """Checks if player hovered a given area with mouse

        Args:
            pos: the players mouses coordinates on screen (x, y)
            x_coord: the left x-coordinate of the area being checked
            y_coord: the top y-coordinate of the area being checked
            width: the width of the area
            height: the height of the area
        
        Returns:
            True if the mouse hovers the area, otherwise False
        """

        if (x_coord + width) >= pos[0] >= x_coord and (y_coord + height) >= pos[1] >= y_coord:
            return True
        return False

    def if_correct_password(self, username, password):
        """Checks if password matches the hashed password in database with the given username

        Args:
            username: the username the user entered when logging in
            password: the password the user entered when logging in
        
        Returns:
            True if password matches, otherwise False
        """

        hashed = self.database.get_hashed_password(username)
        password = password.encode()
        if bcrypt.checkpw(password, hashed):
            print("Password correct")
            return True
        print("Password incorrect")
        return False
