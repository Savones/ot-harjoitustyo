import sqlite3


class Database:
    """A class that changes and gets information from the database
    """

    def __init__(self):
        self.database = sqlite3.connect("player_database.db")
        self.database.isolation_level = None

    def create_table(self):
        self.database.execute(
            "CREATE TABLE Players (name TEXT, password TEXT, high_score INTEGER)"
        )
        self.database.execute(
            "CREATE TABLE Scores (name TEXT, easy INTEGER, medium INTEGER, hard INTEGER)"
        )

    def add_player(self, name, password, high_score):
        self.database.execute(
            "INSERT INTO Players (name, password, high_score) VALUES (?, ?, ?)",
            [name, password, high_score])
        self.database.execute(
            "INSERT INTO Scores (name, easy, medium, hard) VALUES (?, 1, 2, 3)",
            [name])

    def get_players_table(self, difficulty):
        return self.database.execute("SELECT * FROM Scores ORDER BY (%s) DESC" % (difficulty)).fetchall()

    def table_exists(self):
        try:
            self.database.execute("SELECT * FROM Players")
            return True
        except sqlite3.OperationalError:
            return False

    def player_exists(self, p_name):
        try:
            if p_name == self.database.execute("SELECT name FROM Players WHERE name = ?", [
                    p_name]).fetchone()[0]:
                return True
            return False
        except TypeError:
            return False

    def get_high_score(self, p_name):
        high_score = self.database.execute("SELECT high_score FROM Players WHERE name = ?", [
            p_name]).fetchone()[0]
        return high_score

    def get_hashed_password(self, username):
        return self.database.execute("SELECT password FROM Players WHERE name = ?", [username]
                                     ).fetchone()[0]

    def change_high_score(self, p_name, new_high_score):
        self.database.execute(
            "UPDATE Players SET high_score = ? WHERE name = ?", [new_high_score, p_name])
