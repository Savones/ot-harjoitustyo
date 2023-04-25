import bcrypt


class Check:

    def __init__(self, database, squares):
        self.database = database

    def check_click(self, player_input, correct_answer):
        x_coord = 155
        y_coord = 100
        for i in range(1, 10):
            if (x_coord + 90) >= player_input[0] >= x_coord:
                if (y_coord + 90) >= player_input[1] >= y_coord:
                    break
            if i % 3 == 0:
                y_coord += 100
                x_coord = 155
            else:
                x_coord += 100

        if i == correct_answer:
            return True
        return False

    def check_misclick(self, pos):
        found = False
        x_coord = 155
        y_coord = 100
        for i in range(1, 10):
            if (x_coord + 90) >= pos[0] >= x_coord and (y_coord + 90) >= pos[1] >= y_coord:
                found = True
                break
            if i % 3 == 0:
                y_coord += 100
                x_coord = 155
            else:
                x_coord += 100
        return found

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
