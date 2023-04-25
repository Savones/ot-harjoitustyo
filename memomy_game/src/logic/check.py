import bcrypt


class Check:

    def __init__(self, database, squares):
        self.database = database
        self.squares = squares.squares
        self.square_width = squares.square_width

    def check_click(self, player_input, correct_answer):
        correct_x = self.squares[correct_answer][0]
        correct_y = self.squares[correct_answer][1]

        if (correct_x + self.square_width) >= player_input[0] >= correct_x:
            if (correct_y + self.square_width) >= player_input[1] >= correct_y:
                return True
        return False

    def check_misclick(self, pos):
        for square in self.squares:
            if (square[0] + self.square_width) >= pos[0] >= square[0]:
                if (square[1] + self.square_width) >= pos[1] >= square[1]:
                    return True
        return False

    def valid_username(self, username):
        if len(username) >= 7 or len(username) <= 1:
            return False
        return True

    def valid_password(self, password):
        if len(password) >= 20 or len(password) <= 4:
            return False
        return True

    def if_hovered(self, pos, x_coord, y_coord, width, height):
        if (x_coord + width) >= pos[0] >= x_coord and (y_coord + height) >= pos[1] >= y_coord:
            return True
        return False

    def if_correct_password(self, username, password):
        hashed = self.database.get_hashed_password(username)
        password = password.encode()
        if bcrypt.checkpw(password, hashed):
            print("Password correct")
            return True
        print("Password incorrect")
        return False
