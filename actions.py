import random

def stoke_fire(player_values):
    wood = player_values['wood']
    warmth = player_values['warmth']
    hunger = player_values['hunger']
    friends = player_values['friends']
    health = player_values['health']
    anxiety = player_values['anxiety']
    name = player_values['player']
    if int(wood) < 1:
        status = "No wood!"
    else:
        status = "Warm from Stoking Fire"
        if int(friends) < 1:
            warmth = int(warmth) + random.randint(1,10)
            hunger = int(hunger) - random.randint(1,10)
            anxiety = int(anxiety) - random.randint(1,10)
            wood = int(wood) - random.randint(1,10)
        if int(friends) > 1:
            if int(friends) < 5:
                warmth = int(warmth) + (random.randint(1,10) * int(friends))
                hunger = int(hunger) - random.randint(1,10)
                anxiety = int(anxiety) - random.randint(1,10)
                wood = int(wood) - (random.randint(1,10)/int(friends))
        if int(friends) > 5:
            if int(friends) < 10:
                warmth = int(warmth) + (random.randint(1,10) * (int(friends)/2))
                hunger = int(hunger) - random.randint(1,10)
                anxiety = int(anxiety) - (random.randint(1,10)/0.5)
                wood = int(wood) - (random.randint(1,10)/int(friends))
            if int(friends) > 10:
                warmth = int(warmth) + (random.randint(1,10) * (int(friends)/4))
                hunger = int(hunger) - random.randint(1,10)
                anxiety = int(anxiety) - (random.randint(1,10)/2)
                wood = int(wood) - (random.randint(1,10)/int(friends))
    return {'warmth':warmth, 'hunger':hunger,'health':health,'anxiety':anxiety,'friends':friends,'status':status,'wood':wood,'player':name}

def gather_wood(player_values):
    wood = player_values['wood']
    warmth = player_values['warmth']
    hunger = player_values['hunger']
    friends = player_values['friends']
    health = player_values['health']
    anxiety = player_values['anxiety']
    name = player_values['player']
    if int(anxiety) < 5:
        status = "Too Scared to Gather Wood"
    elif int(warmth) < 1:
        status = "Too Cold to Gather Wood"
    else:
        status = "Cold from Gathering Wood"
        if int(friends) < 1:
            warmth = int(warmth) - random.randint(1,10)
            hunger = int(hunger) - random.randint(1,10)
            anxiety = int(anxiety) - random.randint(1,10)
            wood = (int(wood) + random.randint(1,10)) * int(anxiety)
        if int(friends) > 1:
            warmth = int(warmth) - random.randint(1,10)
            hunger = int(hunger) - random.randint(1,10)
            anxiety = int(anxiety) - random.randint(1,10)
            wood = (int(wood) + (random.randint(1,10) * int(friends))) * int(anxiety)
    return {'warmth':warmth, 'hunger':hunger,'health':health,'anxiety':anxiety,'friends':friends,'status':status,'wood':wood, 'player':name}

def gather_food(player_values):
    wood = player_values['wood']
    warmth = player_values['warmth']
    hunger = player_values['hunger']
    friends = player_values['friends']
    health = player_values['health']
    anxiety = player_values['anxiety']
    food = player_values['food']
    name = player_values['player']
    if int(anxiety) < 5:
        status = "Too Scared to Hunt"
    elif int(warmth) < 1:
        status = "Too Cold to Hunt"
    else:
        status = "Cold from Hunting"
        if int(friends) < 1:
            warmth = int(warmth) - random.randint(1,10)
            hunger = int(hunger) - random.randint(1,10)
            anxiety = int(anxiety) - random.randint(1,10)
            food = (int(food) + random.randint(1,10)) * int(anxiety)
        if int(friends) > 1:
            warmth = int(warmth) - random.randint(1,10)
            hunger = int(hunger) - random.randint(1,10)
            anxiety = int(anxiety) - random.randint(1,10)
            food = (int(food) + (random.randint(1,10) * int(friends))) * int(anxiety)
    return {'warmth':warmth, 'hunger':hunger,'health':health,'anxiety':anxiety,'friends':friends,'status':status,'wood':wood, 'food':food,'player':name}

def eat_food(player_values):
    wood = player_values['wood']
    warmth = player_values['warmth']
    hunger = player_values['hunger']
    friends = player_values['friends']
    health = player_values['health']
    anxiety = player_values['anxiety']
    food = player_values['food']
    name = player_values['player']
    if int(warmth) < 1:
        status = "Too Cold to Eat"
    elif int(food) < 1:
        status = "No Food!"
    else:
        status = "Less Hungry from Eating"
        if int(friends) < 1:
            warmth = int(warmth) - random.randint(1,10)
            hunger = int(hunger) + random.randint(1,10)
            anxiety = int(anxiety) - random.randint(1,10)
            food = int(food) - random.randint(1,10)
            health = int(health) + random.randint(1,10)
        if int(friends) > 1:
            warmth = int(warmth) - random.randint(1,10)
            hunger = int(hunger) + (random.randint(1,10) * int(friends))
            anxiety = int(anxiety) - random.randint(1,10)
            food = int(food) - (random.randint(1,10) * int(friends))
            health = int(health) + (random.randint(1,10) * int(friends))
    return {'warmth':warmth, 'hunger':hunger,'health':health,'anxiety':anxiety,'friends':friends,'status':status,'wood':wood, 'food':food,'player':name}

def do_nothing(player_values):
    wood = player_values['wood']
    warmth = player_values['warmth']
    hunger = player_values['hunger']
    friends = player_values['friends']
    health = player_values['health']
    anxiety = player_values['anxiety']
    food = player_values['food']
    name = player_values['player']
    if int(friends) < 1:
        status = "Doing nothing alone..."
        warmth = (int(warmth) + random.randint(1,10)) * int(wood)
        hunger = int(hunger) - random.randint(1,10)
        anxiety = int(anxiety) + random.randint(1,10)
        wood = int(wood) - random.randint(1,10)
    if int(friends) > 1:
        status = "Doing nothing alone..."
        warmth = (int(warmth) + (random.randint(1,10) * int(friends))) * int(wood)
        hunger = int(hunger) - (random.randint(1,10) * int(friends))
        anxiety = int(anxiety) + (random.randint(1,10) * int(friends))
        wood = int(wood) - random.randint(1,10)
    return {'warmth':warmth, 'hunger':hunger,'health':health,'anxiety':anxiety,'friends':friends,'status':status,'wood':wood, 'food':food,'player':name}

if __name__ == '__main__':
    print("This is the game actions library, designed for use with AColdWalk, licensed under the MIT License, (c) James Milne 2015")
