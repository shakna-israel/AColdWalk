import random

def stoke_fire(player_values):
    wood = player_values['wood']
    warmth = player_values['warmth']
    hunger = player_values['hunger']
    friends = player_values['friends']
    health = player_values['health']
    anxiety = player_values['anxiety']
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
    return {'warmth':warmth, 'hunger':hunger,'health':health,'anxiety':anxiety,'friends':friends,'status':status,'wood':wood}

def gather_wood(player_values):
    wood = player_values['wood']
    warmth = player_values['warmth']
    hunger = player_values['hunger']
    friends = player_values['friends']
    health = player_values['health']
    anxiety = player_values['anxiety']
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
            wood = int(wood) + random.randint(1,10)
        if int(friends) > 1:
            warmth = int(warmth) - random.randint(1,10)
            hunger = int(hunger) - random.randint(1,10)
            anxiety = int(anxiety) - random.randint(1,10)
            wood = int(wood) + (random.randint(1,10) * int(friends))
    return {'warmth':warmth, 'hunger':hunger,'health':health,'anxiety':anxiety,'friends':friends,'status':status,'wood':wood}

def gather_food(player_values):
    wood = player_values['wood']
    warmth = player_values['warmth']
    hunger = player_values['hunger']
    friends = player_values['friends']
    health = player_values['health']
    anxiety = player_values['anxiety']
    food = player_values['food']
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
            food = int(food) + random.randint(1,10)
        if int(friends) > 1:
            warmth = int(warmth) - random.randint(1,10)
            hunger = int(hunger) - random.randint(1,10)
            anxiety = int(anxiety) - random.randint(1,10)
            food = int(food) + (random.randint(1,10) * int(friends))
    return {'warmth':warmth, 'hunger':hunger,'health':health,'anxiety':anxiety,'friends':friends,'status':status,'wood':wood, 'food':food}

def eat_food(player_values):
    wood = player_values['wood']
    warmth = player_values['warmth']
    hunger = player_values['hunger']
    friends = player_values['friends']
    health = player_values['health']
    anxiety = player_values['anxiety']
    food = player_values['food']
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
        if int(friends) > 1:
            warmth = int(warmth) - random.randint(1,10)
            hunger = int(hunger) + (random.randint(1,10) * int(friends))
            anxiety = int(anxiety) - random.randint(1,10)
            food = int(food) - (random.randint(1,10) * int(friends))
    return {'warmth':warmth, 'hunger':hunger,'health':health,'anxiety':anxiety,'friends':friends,'status':status,'wood':wood, 'food':food}

def do_nothing(player_values):
    wood = player_values['wood']
    warmth = player_values['warmth']
    hunger = player_values['hunger']
    friends = player_values['friends']
    health = player_values['health']
    anxiety = player_values['anxiety']
    food = player_values['food']
    if int(friends) < 1:
        status = "Doing nothing alone..."
        warmth = int(warmth) + random.randint(1,10)
        hunger = int(hunger) - random.randint(1,10)
        anxiety = int(anxiety) - random.randint(1,10)
    if int(friends) > 1:
        status = "Doing nothing alone..."
        warmth = int(warmth) + (random.randint(1,10) * int(friends))
        hunger = int(hunger) - (random.randint(1,10) * int(friends))
        anxiety = int(anxiety) - (random.randint(1,10) * int(friends))
    return {'warmth':warmth, 'hunger':hunger,'health':health,'anxiety':anxiety,'friends':friends,'status':status,'wood':wood, 'food':food}