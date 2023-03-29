from pattern import Pattern

class ShowPattern:
    def __inti__(self):
        self.grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.pattern_list = Pattern()
    
    def show_pattern(self):
        for item in self.pattern_list:
            pass

    def default_grid(self):
        self.grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]