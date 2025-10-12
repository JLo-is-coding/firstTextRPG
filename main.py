from commands.parse_input import parse_input
from commands.resolve_command import resolve_command
from game_data.pathways import pathways
from gamestate import Gamestate
from err_handling import transform_err

def main():
    print("Initialising...")
    game = Gamestate()

    print("Welcome to JLo's Text RPG!")

    while 0<1:
        resolved = False
        while resolved == False:
            user_input = input("\nwhat would you like to do?\n> ")
            command, target = parse_input(user_input)
            try:
                if target == None:
                    resolve_command(command)()
                elif target != None:
                    resolve_command(command)(target, game)
            except Exception as e:
                print (transform_err(e))

main()