from game.pattern import Pattern
from game.check import Check
from ui.game_ui import Display
from game.loop import Loop
from ui.game_over_ui import GameOverDisplay
from ui.scoreboard_ui import ScoreboardDisplay

from registeration.player_database import Database
from registeration.registeration_loop import RegisterationLoop

def main():
    database = Database()

    registeration_loop = RegisterationLoop(database)
    player = registeration_loop.start()

    pattern = Pattern(player)
    check = Check()
    display = Display()
    game_over_display = GameOverDisplay()
    scoreboard_display = ScoreboardDisplay()

    loop = Loop(pattern, check, display, game_over_display, scoreboard_display)
    loop.start_game()

main()