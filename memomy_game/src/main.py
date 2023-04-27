import os
import pygame

from logic.variables import Variables
from logic.check import Check
from loops.loop import Loop
from loops.registeration_loop import RegisterationLoop
from ui.game_over_ui import GameOverDisplay
from ui.scoreboard_ui import ScoreboardDisplay
from ui.game_ui import Display
from ui.registeration_ui import RegisDisplay
from database.player_database import Database
from objects.squares import Squares

HEIGHT = 600
WIDTH = 600


def main():
    os.remove("player_database.db")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    squares = Squares()
    database = Database()
    check = Check(database, squares)

    while True:
        regis_display = RegisDisplay(screen)

        registeration_loop = RegisterationLoop(database, regis_display, check)
        player = registeration_loop.start()

        variables = Variables(player, database)
        display = Display(screen, player, squares)
        game_over_display = GameOverDisplay(screen)
        scoreboard_display = ScoreboardDisplay(screen, player, database)

        loop = Loop(variables, check, display,
                    game_over_display, scoreboard_display)
        loop.start_game()


main()

# to be added:
# a method that makes sure database doesn't overflow
# a quit button for the game ui
# return button from password view (login left)
# error messages part of graphic ui
# method to make sure clicks during pattern showing dont count

# extras:
# color change
# speed mode
# a countdown before the game starts
# hovering squares changes their color in game
# numbered mode

# switch case
# buttons
# squares
