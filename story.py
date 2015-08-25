import utilities
import essentials

"""A hack-y mess to allow input() on Python 2.x and Python 3.x"""
try:
    input = raw_input
except NameError:
    pass

def check_event(dictIn):
    """If a user has an older save file, a new save file, or a corrupted save file, make it so they start the story"""
    try:
        event = dictIn['event']
    except KeyError:
        event = "none"
    return event

def event_printing(dictIn):
    """Ugly mess that makes writing events easier to read and understand"""
    utilities.screen_clear()
    dictIn = essentials.confirm_values(dictIn)
    dictIn = essentials.value_relationships(dictIn)
    dictIn = essentials.confirm_values(dictIn)
    essentials.pretty_values(dictIn)
    print("---")
    return dictIn

def event_one(dictIn):
    dictIn = event_printing(dictIn)
    print(dictIn['player'] + " was standing by the fire, freezing...")
    input("Press Enter To Continue ")
    dictIn = event_printing(dictIn)
    print("There was a knock at the door...")
    input("Press Enter To Continue ")
    dictIn['anxiety'] = int(dictIn['anxiety']) - 50
    dictIn = event_printing(dictIn)
    print("... There's someone out there...")
    input("Press Enter To Continue ")
    dictIn['anxiety'] = 0
    dictIn = event_printing(dictIn)
    print("... And they want in...")
    input("Press Enter To Continue ")
    dictIn['anxiety'] = 0
    dictIn = event_printing(dictIn)
    choice_string = ("---\n1. Let them in\n"
             "2. Ignore their moans for help\n")
    choice = input(choice_string + dictIn['player'] + " will.......... ")
    if str(choice).strip() == '1':
        dictIn['anxiety'] = 0
        dictIn['stranger'] = 1
        dictIn['event'] = 'one'
        pass
    elif str(choice).strip() == '2':
        dictIn['anxiety'] = 0
        dictIn['event'] = 'none'
        pass
    else:
        dictIn['anxiety'] = 0
        dictIn['event'] = 'none'
        pass
    dictIn = essentials.confirm_values(dictIn)
    dictIn = essentials.value_relationships(dictIn)
    dictIn = essentials.confirm_values(dictIn)
    essentials.save_file(dictIn)
    utilities.screen_clear()
    return True

def event_two(dictIn):
    dictIn = event_printing(dictIn)
    print(dictIn['player'] + " was staring at the stranger shivering in the corner...")
    input("Press Enter To Continue ")
    dictIn = event_printing(dictIn)
    print("The stranger stood up slowly...")
    dictIn['anxiety'] = int(dictIn['anxiety']) - 10
    input("Press Enter To Continue ")
    dictIn = event_printing(dictIn)
    print("They smile slowly, and say... Thankyou.")
    dictIn['anxiety'] = int(dictIn['anxiety']) + 20
    input("Press Enter To Continue ")
    dictIn = event_printing(dictIn)
    dictIn['stranger'] = int(dictIn['stranger']) - 1
    dictIn['friends'] = int(dictIn['friends']) + 1
    dictIn['event'] = 'two'
    dictIn = essentials.confirm_values(dictIn)
    dictIn = essentials.value_relationships(dictIn)
    dictIn = essentials.confirm_values(dictIn)
    essentials.save_file(dictIn)
    utilities.screen_clear()

def event_three(dictIn):
    dictIn = event_printing(dictIn)
    print(dictIn['player'] + " was sitting in the cold, and the quiet.")
    input("Press Enter To Continue ")
    dictIn['anxiety'] = int(dictIn['anxiety']) - 10
    dictIn = event_printing(dictIn)
    print("There was a small distant snuffling sound.")
    input("Press Enter To Continue ")
    dictIn['anxiety'] = int(dictIn['anxiety']) - 10
    dictIn = event_printing(dictIn)
    print("It came closer and closer...")
    input("Press Enter To Continue ")
    dictIn = event_printing(dictIn)

if __name__ == '__main__':
    print("This is the game story library, designed for use with AColdWalk, licensed under the MIT License, (c) James Milne 2015")
