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
    if friend < 0:
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
    if friend < 0:
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
    file.write(newLine)
    #Some sort of for loop?
    file.close()

def load():
    file = open("save.var", "r")
    filedata = file.read()
    #Some sort of for loop? Or specific lines meaning specific variables?
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
loop = 1
while loop == 1:
    actionChoice()
