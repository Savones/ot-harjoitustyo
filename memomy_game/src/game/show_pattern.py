# from pattern import Pattern
# ui:n rajapinta (näyttää patternin pelaajalle)

class ShowPattern:
    
    def show_pattern(self, pattern):
        for item in pattern:
            grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

            grid[item[0]][item[1]] = 1
            for row in grid:
                print(row)
            print()
