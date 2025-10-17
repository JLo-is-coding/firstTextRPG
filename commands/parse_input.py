def parse_input(user_input):
    if user_input == "":
        raise Exception("Please specify a command")
    parts = user_input.split()
    command = parts[0].upper()
    target = " ".join(parts[1:]).lower() if len(parts) > 1 else None
    return command, target