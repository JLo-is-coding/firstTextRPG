from commands.parse_input import parse_input
from commands.resolve_command import resolve_command
from events_handling.process_events import proc_additional_events
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
            
            try:
                command, target = parse_input(user_input)
                if target == None:
                    resolve_command(command)()
                elif target != None:
                    resolve_command(command)(target, game)

                proc_additional_events(command, target, game.location)
                
            except Exception as e:
                print (transform_err(e))

main()

