from game_data.pathways import pathways
from game_data.doors.doors_library import doors

def get_door_id(target, gamestate):
    parts = sorted([target, gamestate.location])
    return f"{parts[0]}-{parts[1]}"

def check_target_room(target, gamestate):
    if target in pathways[gamestate.location]["exits"]:
        return True
    return False

def check_door_state(intended_path):
    if intended_path not in doors:
        return True
    if doors[intended_path].state == "unlocked":
        return True
    return False

def explore(target, gamestate):
    intended_path = get_door_id(target, gamestate)
    if target == gamestate.location:
        raise Exception("You are already there!")
    if not check_target_room(target, gamestate):
        raise Exception("You can't go there...")
    if not check_door_state(intended_path):
        raise Exception("That door is locked.")
    gamestate.move_player(target)