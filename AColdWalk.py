#!/usr/bin/env python
import os
import time

global var_warmth
global var_wood
global var_health
global var_food
global var_anxiety
global username

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

def stokeFire():
    print "The fire warms the room."
    global var_wood
    var_wood = var_wood - 10
    global var_warmth
    var_warmth = var_warmth + 10
    checkValues()

def gatherWood():
    print "It's freezing out here!"
    print "... Lucky there's so much bracken."
    global var_wood
    var_wood = var_wood + 10
    global var_warmth
    var_warmth = var_warmth - 10
    checkValues()

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
print "Enter A to stoke the fire."
print "Enter B to gather more wood."
choice_active = 1
choice = raw_input("... "
while (choice_active == 1):
    if choice == A:
         stokeFire()
         choice_active = 0
    else
        gatherWood()
        choice_active = 0
print raw_input("Press enter to continue.")
clear()
fetch_status()
print raw_input("Press enter to continue.")
