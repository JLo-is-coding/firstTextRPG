from game_data.events.events_library import events


def proc_additional_events(command, target, location):
    trigger = (command, target, location)
    if trigger in events:
        func = events[trigger]["func"]
        func()
        proc_additional_events(events[trigger]["tag"], None, location)
    else: 
        return