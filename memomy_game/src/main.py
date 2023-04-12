import pygame
from game.pattern import Pattern
from game.check import Check
from ui.game_ui import Display
from game.loop import Loop
from ui.game_over_ui import GameOverDisplay
from ui.scoreboard_ui import ScoreboardDisplay

from registeration.player_database import Database
from registeration.registeration_loop import RegisterationLoop
from ui.registeration_ui import RegisDisplay

HEIGHT = 600
WIDTH = 600

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    database = Database()
    check = Check()

    while True:
        regis_display = RegisDisplay(screen)

        registeration_loop = RegisterationLoop(database, regis_display, check)
        player = registeration_loop.start()

        pattern = Pattern(player, database)
        display = Display(screen)
        game_over_display = GameOverDisplay(screen)
        scoreboard_display = ScoreboardDisplay(screen, player, database)

        loop = Loop(pattern, check, display, game_over_display, scoreboard_display)
        loop.start_game()

main()