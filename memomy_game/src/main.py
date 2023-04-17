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

HEIGHT = 600
WIDTH = 600


def main():
    os.remove("player_database.db")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    database = Database()
    check = Check()

    while True:
        regis_display = RegisDisplay(screen)

        registeration_loop = RegisterationLoop(database, regis_display, check)
        player = registeration_loop.start()

        variables = Variables(player, database)
        display = Display(screen)
        game_over_display = GameOverDisplay(screen)
        scoreboard_display = ScoreboardDisplay(screen, player, database)

        loop = Loop(variables, check, display,
                    game_over_display, scoreboard_display)
        loop.start_game()


main()
