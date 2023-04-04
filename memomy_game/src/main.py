from game.pattern import Pattern
from game.check import Check
from ui.game_ui import Display
from game.loop import Loop

def main():
    pattern = Pattern()
    check = Check()
    display = Display()

    loop = Loop(pattern, check, display)
    loop.start()

main()