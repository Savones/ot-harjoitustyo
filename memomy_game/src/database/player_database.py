import sqlite3


class Database:
    """A class that changes and gets information from the database
    """

    def __init__(self):
        """The classes constructor which creates the connection to the database
        """

        self.database = sqlite3.connect("player_database.db")
        self.database.isolation_level = None

    def create_table(self):
        """Creates the Players and Scores tables for the database
        """

        self.database.execute(
            "CREATE TABLE Players (name TEXT, password TEXT)"
        )
        self.database.execute(
            "CREATE TABLE Scores (name TEXT, easy INTEGER, medium INTEGER, hard INTEGER)"
        )

    def add_player(self, name, password):
        """Adds the players information to the database

        Args:
            name: the players username
            password: the players crypted password
        """

        self.database.execute(
            "INSERT INTO Players (name, password) VALUES (?, ?)",
            [name, password])
        self.database.execute(
            "INSERT INTO Scores (name, easy, medium, hard) VALUES (?, 0, 0, 0)",
            [name])

    def get_players_table(self, difficulty):
        """Gets the the list of players highscores on a given difficulty

        Args:
            difficulty: given game difficulty level

        Returns:
            A list of players and their highscores on given difficulty in rank order
        """

        return self.database.execute(
            f"SELECT * FROM Scores ORDER BY {difficulty} DESC").fetchall()

    def table_exists(self):
        """Checks if the Players table exists in the database

        Returns:
            True if table exists, False if it doesn't
        """
        try:
            self.database.execute("SELECT * FROM Players")
            return True
        except sqlite3.OperationalError:
            return False

    def player_exists(self, player):
        """Checks if a username is found in the Players table

        Args:
            player: the players username

        Returns:
            True if username is found, False if not found or table Player not existing
        """
        try:
            if player == self.database.execute("SELECT name FROM Players WHERE name = ?", [
                                                player]).fetchone()[0]:
                return True
            return False
        except TypeError:
            return False

    def get_high_score(self, player, difficulty):
        """Finds the players highscore on a given game difficulty

        Args:
            player: the players username
            difficulty: the given game difficulty

        Returns:
            The players highscore on the difficulty
        """

        high_score = self.database.execute(
            f"SELECT {difficulty.name} FROM Scores WHERE name = ?", [
                                    player]).fetchone()[0]
        return high_score

    def get_hashed_password(self, username):
        """Finds the players crypted password from the Players table

        Args:
            username: the players username

        Returns:
            The players hashed password
        """
        return self.database.execute(
            "SELECT password FROM Players WHERE name = ?", [username]
        ).fetchone()[0]

    def change_high_score(self, player, new_high_score, difficulty):
        """Updates the players highscore on a given difficulty to the Scores table

        Args:
            player: the players username
            new_high_score: the players new highscore
            difficulty: the game difficulty for the new highscore
        """

        self.database.execute(
            f"UPDATE Scores SET {difficulty.name} = ? WHERE name = ?", [
                            new_high_score, player])
