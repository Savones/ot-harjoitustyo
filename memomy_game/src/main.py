from game.pattern import Pattern
from game.show_pattern import ShowPattern
from game.check import Check
from ui.game_ui import Display
from game.loop import Loop

def main():
    pattern = Pattern()
    show_pattern = ShowPattern()
    check = Check()

    loop = Loop(pattern, show_pattern, check)
    loop.start()

main()