import os

def screen_clear():
    """A simple way to clear the screen cross-platform"""
    os.system(['clear','cls'][os.name == 'nt'])

def fetch_input_method():
    """A hack-y mess to allow input() on Python 2.x and Python 3.x"""
    try:
        input = raw_input
    except NameError:
        pass

def exit_handler():
    screen_clear()

if __name__ == '__main__':
    print("This is the system utilities library, designed for use with AColdWalk, licensed under the MIT License, (c) James Milne 2015")