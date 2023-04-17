import os
import sqlite3


class Database:
    def __init__(self):
        self.database = sqlite3.connect("player_database.db")
        self.database.isolation_level = None

    def create_table(self):
        self.database.execute(
            "CREATE TABLE Players (id INTEGER PRIMARY KEY, name TEXT, high_score INTEGER)")

    def add_player(self, name, high_score):
        self.database.execute(
            "INSERT INTO Players (name, high_score) VALUES (?, ?)", [name, high_score])

    def reset_db(self):
        os.remove("player_database.db")

    def get_players_table(self):
        return self.database.execute("SELECT * FROM Players ORDER BY high_score DESC").fetchall()

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

    def change_high_score(self, p_name, new_high_score):
        self.database.execute(
            "UPDATE Players SET high_score = ? WHERE name = ?", [new_high_score, p_name])
