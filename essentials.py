import json
import os
import random

def file_structure():
    if os.path.isdir(os.path.expanduser('~/.AColdWalk')):
        return True
    else:
        os.makedirs(os.path.expanduser('~/.AColdWalk'))

def save_file(dictIn):
    with open(os.path.expanduser('~/.AColdWalk/save'),'w+') as saveFile:
        try:
            saveFile.write(json.dumps(dictIn, sort_keys=True, indent=4, separators=(',', ': ')))
        except ValueError:
            dictIn = {}
            confirm_values({})
            saveFile.write(json.dumps(dictIn, sort_keys=True, indent=4, separators=(',', ': ')))
        saveFile.close()

def load_file():
    try:
        with open(os.path.expanduser('~/.AColdWalk/save'),'r') as saveFile:
            try:
                returnValue = json.load(saveFile)
            except ValueError:
                returnValue = confirm_values({})
            return returnValue
    except (OSError, IOError) as e:
        returnValue = confirm_values({})
        return returnValue

def confirm_values(dictIn):
    """Check all player values make sense."""
    # For the health value
    try:
        dictIn['health']
        if int(dictIn['health']) >99:
            health = 100
        elif int(dictIn['health']) < 1:
            health = 0
        else:
            health = int(dictIn['health'])
    except KeyError:
        health = 100
    dictIn['health'] = health
    # For the hunger value
    try:
        dictIn['hunger']
        if int(dictIn['hunger']) >99:
            hunger = 100
        elif int(dictIn['hunger']) < 1:
            hunger = 0
        else:
            hunger = int(dictIn['hunger'])
    except KeyError:
        hunger = 100
    dictIn['hunger'] = hunger
    # For the warmth value
    try:
        dictIn['warmth']
        if int(dictIn['warmth']) > 99:
            warmth = 100
        elif int(dictIn['warmth']) < 1:
            warmth = 0
        else:
            warmth = int(dictIn['warmth'])
    except KeyError:
        warmth = 100
    dictIn['warmth'] = warmth
    # For the anxiety value
    try:
        dictIn['anxiety']
        if int(dictIn['anxiety']) >99:
            anxiety = 100
        elif int(dictIn['anxiety']) < 1:
            anxiety = 0
        else:
            anxiety = int(dictIn['anxiety'])
    except KeyError:
        anxiety = 100
    dictIn['anxiety'] = anxiety
    # For the number of friends
    try:
        dictIn['friends']
        if int(dictIn['friends']) < 0:
            friends = 0
        else:
            friends = int(dictIn['friends'])
    except KeyError:
        friends = 0
    dictIn['friends'] = friends
    # Value to make the fire essential
    try:
        dictIn['wood']
        if int(dictIn['wood']) > 99:
            wood = 100
        elif int(dictIn['wood']) < 1:
            wood = 0
        else:
            wood = int(dictIn['wood'])
    except KeyError:
        wood = 100
    dictIn['wood'] = wood
    # Value to make the food essential
    try:
        dictIn['food']
        if int(dictIn['food']) >99:
            food = 100
        elif int(dictIn['food']) < 0:
            food = 0
        else:
            food = int(dictIn['food'])
    except KeyError:
        food = 100
    dictIn['food'] = food
    # Value to make returning random statements easier
    try:
        dictIn['status']
        status = str(dictIn['status'])
    except KeyError:
        status = "Doing Nothing"
    dictIn['status'] = status
    # Value to give player a name
    try:
        dictIn['player']
        player_name = str(dictIn['player'])
    except KeyError:
        player_name = "NotSet"
    dictIn['player'] = player_name
    # Value to allow linear story progression
    try:
        dictIn['event']
        event = str(dictIn['event'])
    except KeyError:
        event = "none"
    dictIn['event'] = event
    # Value to allow for strangers in the house
    try:
        dictIn['stranger']
        stranger = str(dictIn['stranger'])
    except KeyError:
        stranger = str(0)
    dictIn['stranger'] = stranger
    # Value to allow for pets in the house
    try:
        dictIn['pet']
        pet = str(dictIn['pet'])
    except KeyError:
        pet = str(0)
    dictIn['pet'] = pet
    # Value to allow for pet names
    try:
        dictIn['petname']
        petname = list(petname)
    except KeyError:
        petname = []
    dictIn['petname'] = petname
    return dictIn

def value_relationships(dictIn):
    health = int(dictIn['health'])
    hunger = int(dictIn['hunger'])
    warmth = int(dictIn['warmth'])
    anxiety = int(dictIn['anxiety'])
    friends = int(dictIn['friends'])
    wood = int(dictIn['wood'])
    food = int(dictIn['food'])
    status = dictIn['status']
    name = dictIn['player']
    event = dictIn['event']
    stranger = int(dictIn['stranger'])
    pet = int(dictIn['pet'])
    if health < 1:
        status = "The doctor found me at death's door..."
        if friends < 1:
            health = 10
        elif pet:
            status = "The barking alerted a passerby..."
            health = 20
        elif friends < 5:
            status = "My friends got me to the doctor just in time..."
            health = 15

    if hunger < 1:
        status = "Soooooooooooooo hungry!"
        health = health - random.randint(1,10)
        hunger = 10

    if warmth < 1:
        status = "Soooooooooooooo cold!"
        health = health - random.randint(1,10)
        warmth = 10

    if anxiety < 1:
        status = "Sssscared... Sooo sssscared..."
        health = health - random.randint(1,10)
        anxiety = 10

    if stranger > 1:
        status = "I'm not freaking out... I'm not freaking out..."
        if pet:
            anxiety = (anxiety * 0.5) / 0.85
        else:
            anxiety = anxiety * 0.5
        if anxiety < 10:
            anxiety = 10

    int(dictIn['health']) = health
    int(dictIn['hunger']) = hunger
    int(dictIn['warmth']) = warmth
    int(dictIn['anxiety']) = anxiety
    int(dictIn['friends']) = friends
    int(dictIn['wood']) = wood
    int(dictIn['food']) = food
    dictIn['status'] = status
    dictIn['player'] = name
    dictIn['event'] = event
    int(dictIn['stranger']) = stranger
    int(dictIn['pet']) = pet
    return dictIn

def pretty_values(dictIn):
    print("Health: " + str(dictIn['health']) + "%")
    print("Warmth: " + str(dictIn['warmth']) + "%")
    print("Food: " + str(dictIn['hunger']) + "%")
    print("Calm: " + str(dictIn['anxiety']) + "%")
    print("---")
    print("Wood: " + str(dictIn['wood']) + '%')
    print("Food: " + str(dictIn['food']) + '%')
    if int(dictIn['friends']) > 0:
        print("Friends: " + str(dictIn['friends']))
    if int(dictIn['stranger']) > 0:
        print("Strangers: " + str(dictIn['stranger']))
    if int(dictIn['pet']) > 0:
        print("Pets: " + str(dictIn['pet']))
    print("---")
    print("Status: " + str(dictIn['status']))

if __name__ == '__main__':
    print("This is the game essentials library, designed for use with AColdWalk, licensed under the MIT License, (c) James Milne 2015")
