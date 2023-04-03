class Check:
    def __init__(self):
        pass

    def check_player_input(self, player_input, correct_answer):
        if player_input == correct_answer:
            return True
        else:
            print(f"Your answer: {player_input}")
            print(f"Correct answer = {correct_answer}")
            return False
