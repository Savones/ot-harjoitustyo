import random

# lisää listaan uuden arvotun painalluksen
# lista kuvaa taulun (peliruudukon) alkioiden (ruutujen) indeksejä

class Pattern:
    def __init__(self):
        self.pattern = []
    
    def add_random_press(self):
        random_row = random.randint(0,2)
        random_column = random.randint(0,2)
        self.pattern.append([random_row, random_column])




if __name__ == "__main__":
    test_pattern = Pattern()
    for i in range(10):
        test_pattern.add_random_press()
    print(test_pattern.pattern)