class Check:

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
    
    def check_try_again_pos(self, pos):
        if (75 + 200) >= pos[0] >= 85 and (405 + 60) >= pos[1] >= 405:
            return True
        else:
            return False

    def check_scoreboard_pos(self, pos):
        if (325 + 200) >= pos[0] >= 325 and (405 + 60) >= pos[1] >= 405:
            return True
        else:
            return False
    
    def check_return_pos(self, pos):
        if (450 + 120) >= pos[0] >= 450 and (25 + 45) >= pos[1] >= 25:
            return True
        else:
            return False
    
    def check_enter_pos(self, pos):
        if (340 + 150) >= pos[0] >= 340 and (340 + 60) >= pos[1] >= 340:
            return True
        else:
            return False
        
    def check_logout_pos(self, pos):
        if (450 + 120) >= pos[0] >= 450 and (25 + 45) >= pos[1] >= 25:
            return True
        else:
            return False