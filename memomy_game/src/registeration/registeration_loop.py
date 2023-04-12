import pygame
import random

class RegisterationLoop:
    def __init__(self, database):
        self.database = database
    
    def start(self):

        # self.database.reset_db()

        if self.database.table_exists() == False:
            self.database.create_table()

        player_input = input("User name: ")
        
        if not self.database.player_exists(player_input):
            self.database.add_player(player_input, 0)

        return player_input
