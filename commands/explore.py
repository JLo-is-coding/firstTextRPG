from game_data.pathways import pathways
from game_data.doors.doors_library import doors

def check_target_room(target, gamestate):
    if target in pathways[gamestate.location]["exits"]:
        return True
    return False

def check_door_state(intended_path):
    if doors[intended_path].state == "unlocked":
        return True
    return False

def explore(target, gamestate):
    intended_path = f"{gamestate.location}-{target}"
    if not check_target_room(target, gamestate):
        raise Exception("You can't go there...")
    if not check_door_state(intended_path):
        raise Exception("That door is locked.")
    gamestate.move_player(target)