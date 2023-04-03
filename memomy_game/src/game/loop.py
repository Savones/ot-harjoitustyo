
class Loop:

    def __init__(self, pattern, show_pattern, check):
        self.pattern = pattern
        self.show_pattern = show_pattern
        self.check = check

    def start(self):

        # breaks when player fails, every new loop is new level
        while True:
            over = False
            self.pattern.add_random_press()
            # rn is a text ui, should become graphic ui
            self.show_pattern.show_pattern(self.pattern.pattern_list)

            # breaks when player fails or gets to next level by getting the pattern correct
            for i in range(len(self.pattern.pattern_list)):
                # rn player input is text and not clicking on graphic ui      
                player_input_row = int(input(f"{i + 1}. row: "))
                player_input_column = int(input(f"{i + 1}. column: "))
                player_input = [player_input_row, player_input_column]
                bool = self.check.check_player_input(player_input, self.pattern.pattern_list[i])

                if bool == False:
                    print("Game over")
                    over = True
                    break

            if over:
                break




if __name__ == "__main__":
    loop = Loop()
    loop.start()