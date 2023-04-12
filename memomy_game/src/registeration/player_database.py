import os
import sqlite3


class Database:
    def __init__(self):
        self.db = sqlite3.connect("player_database.db")
        self.db.isolation_level = None


    def create_table(self):
        self.db.execute("CREATE TABLE Players (id INTEGER PRIMARY KEY, name TEXT, hs INTEGER)")
    

    def add_player(self, name, hs):
        self.db.execute("INSERT INTO Players (name, hs) VALUES (?, ?)", [name, hs])


    def reset_db(self):
        os.remove("player_database.db")


    def get_players_table(self):    
        return self.db.execute("SELECT * FROM Players ORDER BY hs DESC").fetchall()


    def table_exists(self):
        try:
            self.db.execute("SELECT * FROM Players")
            return True
        except:
            return False
    

    def player_exists(self, p_name):
        try:
            if p_name ==  self.db.execute("SELECT name FROM Players WHERE name = ?", [p_name]).fetchone()[0]:
                return True
            else:
                return False
        except:
            return False


    def get_hs(self, p_name):
        try:
            hs = self.db.execute("SELECT hs FROM Players WHERE name = ?", [p_name]).fetchone()[0]
            return hs
        except:
            print("Error")
    
    
    def change_hs(self, p_name, new_hs):
        try:
            self.db.execute("UPDATE Players SET hs = ? WHERE name = ?", [new_hs, p_name])
        except:
            print("Error")