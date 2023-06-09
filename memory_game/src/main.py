import pygame

from logic.variables import Variables
from logic.check import Check
from logic.make_buttons import Makebuttons
from loops.loop import Loop
from loops.registeration_loop import RegisterationLoop
from ui.game_over_ui import GameOverDisplay
from ui.scoreboard_ui import ScoreboardDisplay
from ui.game_ui import Display
from ui.settings_ui import SettingsDisplay
from ui.registeration_ui import RegisDisplay
from database.player_database import Database
from objects.squares import Squares

HEIGHT = 600
WIDTH = 600


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Memory Game')

    game_buttons = [Makebuttons(0).buttons, Makebuttons(1).buttons, Makebuttons(2).buttons,
                    Makebuttons(4).buttons]
    regis_buttons = Makebuttons(3).buttons

    squares = Squares()
    database = Database()
    check = Check(database, squares)

    while True:
        regis_display = RegisDisplay(screen, regis_buttons)
        registeration_loop = RegisterationLoop(
            database, regis_display, check, regis_buttons)
        player = registeration_loop.start_log_in()

        variables = Variables(player, database)
        displays = [Display(screen, player, squares), SettingsDisplay(screen, game_buttons[3]),
                    GameOverDisplay(screen, game_buttons[1]),
                    ScoreboardDisplay(screen, player, database, game_buttons[2])]

        loop = Loop(variables, check, displays, game_buttons)
        loop.start_game()

main()
