from pattern import Pattern
from player import Player

class Check:
    def __init__(self):
        pass

    def check_player_input(self, player_input, correct_answer):
        if player_input == str(correct_answer):
            return True
        else:
            print(f"Correct answer = {correct_answer}")
            return False
