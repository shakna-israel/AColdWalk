def check_event(dictIn):
    try:
        event = dictIn['event']
    except KeyError:
        event = none
    return event

def event_one(dictIn):
    print("Story Events are Not Yet Implemented")
    return False

if __name__ == '__main__':
    print("This is the game story library, designed for use with AColdWalk, licensed under the MIT License, (c) James Milne 2015")
