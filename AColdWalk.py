#!/usr/bin/env python
import os
import time
import random

global var_warmth
global var_wood
global var_health
global var_food
global var_anxiety
global username
global stranger
global friend

def clear():
    os.system(['clear','cls'][os.name == 'nt'])

def init():
    global var_warmth
    var_warmth = 50
    global var_wood
    var_wood = 100
    global var_health
    var_health = 100
    global var_food
    var_food = 80
    global var_anxiety
    var_anxiety = 10
    global stranger
    stranger = 0
    global friend
    friend = 0

def fetch_status():
    checkValues()
    print "Body Warmth: " + str(var_warmth) + "%"
    print "Wood Stockpile: " + str(var_wood) + "%"
    print "Health: " + str(var_health) + "%"
    print "Food Stockpile: " + str(var_food) + "%"
    print "Anxiety Level: " + str(var_anxiety) + "%"
    print ""
    print ""

def checkValues():
    global var_wood
    if var_wood >= 100:
        var_wood = 100
    if var_wood <= 0:
        var_wood = 0
    global var_warmth
    if var_warmth >= 100:
        var_warmth = 100
    if var_warmth <= 0:
        var_warmth = 0
    global var_health
    if var_health >= 100:
        var_health = 100
    if var_health <= 0:
        var_health = 0
    global var_food
    if var_food >= 100:
        var_food = 100
    if var_food <= 0:
        var_food = 0
    global var_anxiety
    if var_anxiety >= 100:
        var_anxiety = 100
    if var_anxiety <= 0:
        var_anxiety = 0
    global stranger
    if stranger >= 1:
        var_anxiety = var_anxiety + random.randint(0, 5)
    global friend
    if friend >= 1:
        var_anxiety = var_anxiety - friend

def stokeFire():
    clear()
    if friend < 1:
        print "The fire warms the room."
        global var_wood
        var_wood = var_wood - random.randint(0,10)
        global var_warmth
        var_warmth = var_warmth + random.randint(0,10)
    if friend == 1:
        print "The cold brings friends together."
        global var_wood
        var_wood = var_wood - random.randint(0,5)
        global var_warmth
        var_warmth + random.randint(5,10)
    if friend > 1:
        print "Nothing is warmer than friendship."
        global var_wood
        global friend
        friend_multiplier = friend * random.randint(0,10)
        friend_divider = friend / random.randint(0,10)
        var_wood = var_wood - random.randint(0,friend_divider)
        global var_warmth
        var_warmth + random.randint(friend_multiplier,friend_multiplier)

def gatherWood():
    clear()
    if friend < 1:
        print "It's freezing out here!"
        print "... Lucky there's so much bracken."
        global var_wood
        var_wood = var_wood + random.randint(0,10)
        global var_warmth
        var_warmth = var_warmth - random.randint(0,10)
    if friend == 1:
        print "It might be cold, but at least you have company."
        global var_wood
        var_wood = var_wood + random.randint(5,10)
        global var_warmth
        var_warmth = var_warmth - random.randint(0,10)
    if friend > 1:
        print "Many hands make light work."
        global var_wood
        global friend
        var_wood = var_wood + random.randint(0,friend)
        global var_warmth
        var_warmth = var_warmth - random.randint(0,10)

def save():
    file = open("save.var", "w")
    global var_warmth
    global var_wood
    global var_health
    global var_food
    global var_anxiety
    global username
    global stranger
    global friend
    file.write(str(var_warmth))
    file.write("\n")
    file.write(str(var_wood))
    file.write("\n")
    file.write(str(var_health))
    file.write("\n")
    file.write(str(var_food))
    file.write("\n")
    file.write(str(var_anxiety))
    file.write("\n")
    file.write(str(username))
    file.write("\n")
    file.write(str(stranger))
    file.write("\n")    
    file.write(str(friend))
    file.write("\n")
    file.close()

def load():
    global var_warmth
    global var_wood
    global var_health
    global var_food
    global var_anxiety
    global username
    global stranger
    global friend
    var_warmth = 0
    var_wood = 0
    var_health = 0
    var_food = 0
    var_anxiety = 0
    username = 0
    stranger = 0
    friend = 0
    file = open("save.var", "r")
    i = 0
    for line in file.read().split('\n'):
	if i == 0:
            line = var_warmth
        elif i == 1:
            line = var_wood
        elif i == 2:
            line = var_health
        elif i == 3:
            line = var_food
        elif i == 4:
            line = var_anxiety
        elif i == 5:
            line = username
        elif i == 6:
            line = stranger
        elif i == 7:
            line = friend
        i = i + 1
    file.close()

def actionChoice():
    checkValues()
    clear()
    fetch_status()
    if friend < 1:
        print "Enter A to stoke the fire."
        print "Enter B to gather more wood."
    elif friend == 1:
        print "Enter A to snuggle by the fire."
        print "Enter B to gather wood together."
    elif friend >= 1:
        print "Enter A to group by the fire."
        print "Enter B to gather wood together."
    print "Enter S to save."
    choice_active = 1
    while (choice_active == 1):
        choice = raw_input("... ")
        if choice == 'A':
            stokeFire()
            choice_active = 0
        elif choice == 'a':
            stokeFire()
            choice_active = 0
        elif choice == 'B':
            gatherWood()
            choice_active = 0
        elif choice == 'b':
            gatherWood()
            choice_active = 0
        elif choice == 'S':
            save()
            print "Saved"
        elif choice == 's':
            save()
            print "Saved"
    print raw_input("Press enter to continue.")
    clear()

clear()
print "A Cold Walk"
time.sleep(1)
print ""
print ""
print "jm | Design"
time.sleep(1)
clear()
print "Loading"
time.sleep(1)
clear()
print "Loading."
time.sleep(1)
clear()
print "Loading.."
time.sleep(1)
clear()
print "Loading..."
time.sleep(1)
clear()
print "Enter 1 to load."
print "Enter 2 for a New Game."
choice_active = "active"
while (choice_active == "active"):
    choice = raw_input("... ")
    if choice == '1':
        load()
    elif choice == '2':
        new_game()

def new_game():
    init()
    print "... What is your name?"
    global username
    username = raw_input("... ")
    clear()
    print "It all happened on a cold day in July."
    print ""
    print "... I mean a REALLY cold day."
    print "The rain would move to hail and back without warning."
    print ""
    print ""
    print raw_input("Press enter to continue.")
    clear()
    print "The rain just kept coming down, and the day kept getting colder."
    print ""
    print ""
    print "... The cabin I, " + username + ", was staying in... I guess you could say it wasn't going to stay in one piece much longer."
    print raw_input("Press enter to continue.")
    clear()
    fetch_status()
    loop = random.randint(0,20)
    while loop > 1:
         loop = loop - 1
         actionChoice()
    event1()

def event1():
     clear()
     print "The wind has picked up, the cabin is really not liking it."
     print ""
     print "Is it hailing again?"
     print ""
     print ""
     print raw_input("Press enter to continue.")
     clear()
     print "Oh hell..."
     print ""
     print ""
     print raw_input("Press enter to continue.")
     clear()
     print "Oh hell..."
     print ""
     print "There's someone at the door..."
     print ""
     print ""
     print raw_input("Press enter to continue.")
     clear()
     print "I..."
     print ""
     print ""
     print raw_input("Press enter to continue.")
     clear()
     print "I... I guess I can't leave them out there."
     print ""
     print "Not in this weather."
     print ""
     print ""
     print raw_input("Press enter to continue.")
     clear()
     print "I opened the door, and the stranger stumbled in."
     global stranger
     stranger = 1
     print ""
     print "They collapsed by the fire and passed out..."
     print ""
     print ""
     print raw_input("Press enter to continue.")
     clear()
     fetch_status()
     loop = random.randint(0,20)
     while loop > 1:
         loop = loop - 1
         actionChoice()
     event2()

def event2():
     clear()
     print "The stranger by the fire is waking up..."
     print ""
     print ""
     print raw_input("Press enter to continue.")
     clear()
     global var_anxiety
     var_anxiety = var_anxiety + var_anxiety
     fetch_status()
     print ""
     print "The stranger turns to me and smiles weakly... "
     print ""
     print raw_input("Press enter to continue.")
     clear()
     var_anxiety = var_anxiety + var_anxiety
     fetch_status()
     print ""
     print "The stranger turns to me and smiles weakly... and aplogises."
     print ""
     print ""
     print raw_input("Press enter to continue.")
     var_anxiety = random.randint(0,20)
     fetch_status()
     print ""
     print "They say their name is Amanda Lovine. They got caught in the storm."
     global username
     print "I say my name is " + username
     print "Amanda says she can help with the wood and the fire."
     print ""
     print ""
     print raw_input("Press enter to continue.")
     clear()
     loop = random.randint(0,50)
     while loop > 1:
         loop = loop - 1
         actionChoice()
     clear()
     event3()

def event3():
    print "After all that, Amanda and I?"
    print ""
    print "We're friends."
    print ""
    print ""
    print raw_input("Press enter to continue.")
    global stranger
    stranger = stranger - 1
    global friend
    friend = friend + 1
    clear()
    loop = random.randint(0,100)
    while loop > 1:
        loop = loop - 1
        actionChoice()
    clear()
