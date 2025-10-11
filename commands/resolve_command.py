from commands.explore import *

# test func
def display():
    print ("=====Random Display Bullshit=====")
# =============

def resolve_command(command):
    if command == "EXPLORE":
        return explore
    if command == "DISPLAY":
        return display
    raise Exception (f"{command} isn't a valid command.")