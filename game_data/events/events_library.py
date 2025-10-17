from game_data.events.events_functions.events_test import *

events = {
    ("EXPLORE", "library", "spawn") : {
        "func" : test_event,
        "tag" : "test_event",
        "priority" : 1,
        "overide" : False,
        "only-once" : False
    },
    ("EXPLORE", "laboratory", "spawn") : {
        "func" : interupting_event,
        "tag" : "interupting_event",
        "priority" : 1,
        "overide" : True,
        "only-once" : True
    },
    ("EXPLORE", "library", "library") : {
        "func" : test_event,
        "tag" : "test_event",
        "priority" : 2, 
        "overide" : False,
        "only-once" : False
    },
    ("test_event", None, "library") : {
        "func" : test_2,
        "tag" : "test_2",
        "priority" : 2,
        "overide" : False,
        "only-once" : True
    }
}