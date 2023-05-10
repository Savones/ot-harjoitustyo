
class Difficulties:
    """A class that initializes the chosen difficulty

    Attributes:
        difficulty: The chosen game difficulty
    """
        
    def __init__(self, difficulty):
        """The classes constructor which sets the difficulties values

        Args:
            Listed above
        """

        self.name = difficulty
        self.speed = 0
        self. addition = 0
        self.column = 0
        if difficulty == "EASY":
            self.easy()
        elif difficulty == "MEDIUM":
            self.medium()
        else:
            self.hard()

    def easy(self):
        """Initializes the classes variables for easy difficulty
        """

        self.speed = 300
        self.addition = 1
        self.column = 1

    def medium(self):
        """Initializes the classes variables for medium difficulty
        """
        
        self.speed = 200
        self.addition = 2
        self.column = 2

    def hard(self):
        """Initializes the classes variables for hard difficulty
        """
        
        self.speed = 150
        self.addition = 3
        self.column = 3