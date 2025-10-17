from game_data.events.events_functions.events_test import *

events = {
    ("EXPLORE", "library", "library") : {
        "func" : test_event,
        "tag" : "test_event"
    },
    ("test_event", None, "library") : {
        "func" : test_2,
        "tag" : "test_2"
    }
}