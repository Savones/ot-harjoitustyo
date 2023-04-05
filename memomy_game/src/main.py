from game.pattern import Pattern
from game.check import Check
from ui.game_ui import Display
from game.loop import Loop
from ui.game_over_ui import GameOverDisplay

def main():
    pattern = Pattern()
    check = Check()
    display = Display()
    game_over_display = GameOverDisplay()
    loop = Loop(pattern, check, display, game_over_display)
    loop.start()

main()