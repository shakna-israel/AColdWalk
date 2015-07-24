import os

def screen_clear():
    """A simple way to clear the screen cross-platform"""
    os.system(['clear','cls'][os.name == 'nt'])

def exit_handler():
    screen_clear()

if __name__ == '__main__':
    print("This is the system utilities library, designed for use with AColdWalk, licensed under the MIT License, (c) James Milne 2015")
