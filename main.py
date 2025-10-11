from commands.parse_input import parse_input

def main():
    print("Initialising...")
    print("Welcome to JLo's Text RPG!")

    while 0<1:
        user_input = input("what would you like to do?\n> ")
        command, target = parse_input(user_input)

main()