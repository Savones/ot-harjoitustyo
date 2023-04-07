from game.pattern import Pattern
from game.check import Check
from ui.game_ui import Display
from game.loop import Loop
from ui.game_over_ui import GameOverDisplay
from ui.scoreboard_ui import ScoreboardDisplay

def main():
    pattern = Pattern()
    check = Check()
    display = Display()
    game_over_display = GameOverDisplay()
    scoreboard_display = ScoreboardDisplay()


    loop = Loop(pattern, check, display, game_over_display, scoreboard_display)
    loop.start_game()

main()