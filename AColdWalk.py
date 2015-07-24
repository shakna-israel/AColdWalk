import utilities
from essentials import file_structure, save_file, load_file, confirm_values, pretty_values, value_relationships
import actions
import story
import atexit
import random

def game_init():
    utilities.fetch_input_method()
    file_structure()
    save_data = load_file()
    save_data = confirm_values(save_data)
    save_file(save_data)
    return save_data

def game_choices(player_values):
    utilities.screen_clear()
    if story.check_event(player_values) == 'none':
        if random.randint(1,5) == int('5'):
            story.event_one()
            player_values['event'] = 'one'
    pretty_values(player_values)
    choice_string = ("---\n1. Gather Wood\n"
             "2. Stoke the Fire\n"
             "3. Hunt\n"
             "4. Eat\n"
             "5. Do nothing\n")
    choice = input(choice_string + player_name + " will.......... ")
    if str(choice).strip() == '1':
        player_values = actions.gather_wood(player_values)
        pass
    elif str(choice).strip() == '2':
        player_values = actions.stoke_fire(player_values)
        pass
    elif str(choice).strip() == '3':
        player_values = actions.gather_food(player_values)
        pass
    elif str(choice).strip() == '4':
        player_values = actions.eat_food(player_values)
        pass
    elif str(choice).strip() == '5':
        player_values = actions.do_nothing(player_values)
        pass
    else:
        player_values = actions.do_nothing(player_values)
        pass
    player_values = confirm_values(player_values)
    player_values = value_relationships(player_values)
    player_values = confirm_values(player_values)
    save_file(player_values)
    game_choices(player_values)

if __name__ == "__main__":
    utilities.screen_clear()
    atexit.register(utilities.exit_handler)
    player_values = game_init()
    print("A Cold Walk")
    print("(c) James Milne 2015")
    input("Press Enter To Continue ")
    utilities.screen_clear()
    # Set the player name if it doesn't already exist:
    player_name = player_values['player']
    if player_name == "NotSet":
        player_name = input("What is your name? ")
        player_values['player'] = str(player_name)
        player_name = player_values['player']
        player_values = confirm_values(player_values)
        player_values = value_relationships(player_values)
        player_values = confirm_values(player_values)
        save_file(player_values)

    game_choices(player_values)
