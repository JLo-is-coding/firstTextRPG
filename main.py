from commands.parse_input import parse_input
from commands.resolve_command import resolve_command

def main():
    print("Initialising...")
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
                    resolve_command(command)(target)
            except Exception:
                print ("Sorry I didn't understand that command")

main()