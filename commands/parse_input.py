def parse_input(user_input):
    parts = user_input.split()
    command = parts[0].upper()
    target = " ".join(parts[1:]).lower() if len(parts) > 1 else None
    return command, target