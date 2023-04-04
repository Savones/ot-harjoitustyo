class Check:
    def __init__(self):
        pass

    def check_click(self, player_input, correct_answer):
        x = 155
        y = 100
        for i in range(1, 10):
            if (x + 90) >= player_input[0] >= x and (y + 90) >= player_input[1] >= y:
                break
            if i % 3 == 0:
                y += 100
                x = 155
            else:
                x += 100
        
        if i == correct_answer:
            return True
        else:
            return False

    def check_misclick(self, pos):
        found = False
        x = 155
        y = 100
        for i in range(1, 10):
            if (x + 90) >= pos[0] >= x and (y + 90) >= pos[1] >= y:
                found = True
                break
            if i % 3 == 0:
                y += 100
                x = 155
            else:
                x += 100
        
        return found