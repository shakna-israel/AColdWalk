import random

def stoke_fire(player_values):
    wood = player_values['wood']
    warmth = player_values['warmth']
    hunger = player_values['hunger']
    friends = player_values['friends']
    anxiety = player_values['anxiety']
    pet = player_values['pet']
    if int(wood) < 1:
        status = "No wood!"
    else:
        status = "Warm from Stoking Fire"
        if int(friends) < 1:
            warmth = (int(warmth) + int(pet)) + random.randint(1,4)
            hunger = int(hunger) - random.randint(1,4)
            anxiety = (int(anxiety) + int(pet)) - random.randint(1,2)
            wood = int(wood) - random.randint(1,4)
        elif int(friends) > 0:
            if int(friends) < 5:
                warmth = (int(warmth) + int(pet)) + (random.randint(1,4) * int(friends))
                hunger = int(hunger) - random.randint(1,4)
                anxiety = (int(anxiety) + int(pet)) - random.randint(1,2)
                wood = int(wood) - (random.randint(1,4)/int(friends))
        elif int(friends) > 5:
            if int(friends) < 10:
                warmth = (int(warmth) + int(pet)) + (random.randint(1,4) * (int(friends)/2))
                hunger = int(hunger) - random.randint(1,4)
                anxiety = (int(anxiety) + int(pet)) - (random.randint(1,2)/0.5)
                wood = int(wood) - (random.randint(1,4)/int(friends))
            elif int(friends) > 10:
                warmth = (int(warmth) + int(pet)) + (random.randint(1,4) * (int(friends)/4))
                hunger = int(hunger) - random.randint(1,4)
                anxiety = (int(anxiety) + int(pet)) - (random.randint(1,2)/2)
                wood = int(wood) - (random.randint(1,4)/int(friends))
    player_values['wood'] = wood
    player_values['warmth'] = warmth
    player_values['hunger'] = hunger
    player_values['friends'] = friends
    player_values['anxiety'] = anxiety
    player_values['pet'] = pet
    return player_values

def gather_wood(player_values):
    wood = player_values['wood']
    warmth = player_values['warmth']
    hunger = player_values['hunger']
    friends = player_values['friends']
    anxiety = player_values['anxiety']
    pet = player_values['pet']
    if int(anxiety) < 5:
        status = "Too Scared to Gather Wood"
    elif int(warmth) < 1:
        status = "Too Cold to Gather Wood"
    else:
        status = "Cold from Gathering Wood"
        if int(friends) < 1:
            warmth = (int(warmth) + int(pet)) - random.randint(1,4)
            hunger = int(hunger) - random.randint(1,4)
            anxiety = (int(anxiety) + int(pet)) - random.randint(1,2)
            wood = (int(wood) + random.randint(1,4)) * int(anxiety)
        if int(friends) > 0:
            warmth = (int(warmth) + int(pet)) - random.randint(1,4)
            hunger = int(hunger) - random.randint(1,4)
            anxiety = (int(anxiety) + int(pet)) - random.randint(1,2)
            wood = (int(wood) + (random.randint(1,4) * int(friends))) * int(anxiety)
    player_values['wood'] = wood
    player_values['warmth'] = warmth
    player_values['hunger'] = hunger
    player_values['friends'] = friends
    player_values['anxiety'] = anxiety
    player_values['pet'] = pet
    return player_values

def gather_food(player_values):
    wood = player_values['wood']
    warmth = player_values['warmth']
    hunger = player_values['hunger']
    friends = player_values['friends']
    anxiety = player_values['anxiety']
    food = player_values['food']
    pet = player_values['pet']
    if int(anxiety) < 5:
        status = "Too Scared to Hunt"
    elif int(warmth) < 1:
        status = "Too Cold to Hunt"
    else:
        status = "Cold from Hunting"
        if int(friends) < 1:
            warmth = (int(warmth) + int(pet)) - random.randint(1,4)
            hunger = int(hunger) - random.randint(1,4)
            anxiety = (int(anxiety) + int(pet)) - random.randint(1,2)
            food = (int(food) + random.randint(1,4)) * int(anxiety)
        if int(friends) > 0:
            warmth = (int(warmth) + int(pet)) - random.randint(1,4)
            hunger = int(hunger) - random.randint(1,4)
            anxiety = (int(anxiety) + int(pet)) - random.randint(1,2)
            food = (int(food) + (random.randint(1,4) * int(friends))) * int(anxiety)
    player_values['wood'] = wood
    player_values['warmth'] = warmth
    player_values['hunger'] = hunger
    player_values['friends'] = friends
    player_values['anxiety'] = anxiety
    player_values['food'] = food
    player_values['pet'] = pet
    return player_values

def eat_food(player_values):
    wood = player_values['wood']
    warmth = player_values['warmth']
    hunger = player_values['hunger']
    friends = player_values['friends']
    health = player_values['health']
    anxiety = player_values['anxiety']
    food = player_values['food']
    pet = player_values['pet']
    if int(warmth) < 1:
        status = "Too Cold to Eat"
    elif int(food) < 1:
        status = "No Food!"
    else:
        status = "Less Hungry from Eating"
        if int(friends) < 1:
            warmth = (int(warmth) + int(pet)) - random.randint(1,4)
            hunger = int(hunger) + random.randint(1,4)
            anxiety = (int(anxiety) + int(pet)) - random.randint(1,2)
            food = int(food) - random.randint(1,4)
            health = int(health) + random.randint(1,4)
        if int(friends) > 0:
            warmth = (int(warmth) + int(pet)) - random.randint(1,4)
            hunger = int(hunger) + (random.randint(1,4) * int(friends))
            anxiety = (int(anxiety) + int(pet)) - random.randint(1,2)
            food = int(food) - (random.randint(1,4) * int(friends))
            health = int(health) + (random.randint(1,4) * int(friends))
    player_values['wood'] = wood
    player_values['warmth'] = warmth
    player_values['hunger'] = hunger
    player_values['friends'] = friends
    player_values['health'] = health
    player_values['anxiety'] = anxiety
    player_values['food'] = food
    player_values['pet'] = pet
    return player_values

def do_nothing(player_values):
    wood = player_values['wood']
    warmth = player_values['warmth']
    hunger = player_values['hunger']
    friends = player_values['friends']
    anxiety = player_values['anxiety']
    food = player_values['food']
    status = player_values['status']
    pet = player_values['pet']
    if int(pet) > 0:
        status = "Cuddling..."
        warmth = ((int(warmth) + int(pet)) + (random.randint(1,4) * int(friends))) * int(wood)
        hunger = int(hunger) - (random.randint(1,4) * int(friends))
        anxiety = (int(anxiety) + int(pet)) + (random.randint(4,8) * int(friends))
        wood = int(wood) - random.randint(1,4)
    elif int(friends) < 1:
        status = "Doing nothing..."
        warmth = ((int(warmth) + int(pet)) + random.randint(1,4)) * int(wood)
        hunger = int(hunger) - random.randint(1,4)
        anxiety = (int(anxiety) + int(pet)) + random.randint(4,8)
        wood = int(wood) - random.randint(1,4)
    elif int(friends) > 0:
        status = "Doing nothing with friends..."
        warmth = ((int(warmth) + int(pet)) + (random.randint(1,4) * int(friends))) * int(wood)
        hunger = int(hunger) - (random.randint(1,4) * int(friends))
        anxiety = (int(anxiety) + int(pet)) + (random.randint(4,8) * int(friends))
        wood = int(wood) - random.randint(1,4)
    elif int(stranger) > 1:
        status = "Doing nothing... With a freak in the house..."
        warmth = ((int(warmth) + int(pet)) + random.randint(1,4)) * int(wood)
        hunger = int(hunger) - random.randint(1,4)
        anxiety = (int(anxiety) + int(pet)) - (stranger * (random.randint(1,2) / 10))
        wood = int(wood) - random.randint(1,4)
    player_values['wood'] = wood
    player_values['warmth'] = warmth
    player_values['hunger'] = hunger
    player_values['friends'] = friends
    player_values['anxiety'] = anxiety
    player_values['food'] = food
    player_values['status'] = status
    player_values['pet'] = pet
    return player_values

if __name__ == '__main__':
    print("This is the game actions library, designed for use with AColdWalk, licensed under the MIT License, (c) James Milne 2015")
