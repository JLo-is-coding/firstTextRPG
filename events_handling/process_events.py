from game_data.events.events_library import events


def proc_additional_events(command, target, gamestate, priority):
    trigger = (command, target, gamestate.location)
    if (trigger in events) and (events[trigger]["priority"] == priority) and (trigger not in gamestate.triggered_finite_events):
        func = events[trigger]["func"]
        func()
        if events[trigger]["only-once"] == True:
            gamestate.track_event(trigger)
        if events[trigger]["overide"] == True:
            raise Exception
        proc_additional_events(events[trigger]["tag"], None, gamestate, priority)
    else: 
        return