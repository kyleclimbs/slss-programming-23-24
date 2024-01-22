# Kyle Li
# Jan 8 2024

# Create a function called winter holiday
# one parameter - string
# summary of one event from your winter break
# no chatgpt

import random

def winter_holiday(good_or_bad: str) -> str:
    """Give a summary of our winter holidays 2023/24
    
    Params:
        good_or_bad - string that indicates whether the event
            is good or bad
    Returns:
        an event that happened to you during the holidays
        the event is selected part
    """
# Create a list of good and bad events
    good_events = [
        "I watched alot of movies",
        "It was my birthday",
        "Ate alot of good food",
        "Slept alot"

    ]
    bad_events = [
        "I worked alot",
        "Spent alot of money",
        "Didn't get anything from Santa"
    ]

    if good_or_bad.strip().lower() == "good":
        return random.choice(good_events)
    
    if good_or_bad.strip().lower() == "bad":
        return random.choice(bad_events)
    # If the event is good, return a good event
    # Todo: Return a randomly chosen good event
    if good_or_bad.strip().lower() == "good":
        return "Made lots of money."

    # If the event is bad, return a bad event
    
    else: good_or_bad.strip().lower() == "bad"
    return "Naughty children."

def main() -> None:
    # Runs all the things we want to test in our .py file
    print(winter_holiday("good"))
    # "I got a Lego set for the first time in a long time"
    # "I went to Richmond Centre to walk around aimlessly."
    print(winter_holiday("bad"))
    # "I hoped to snowboard during the holiday and there was only rain."
    #"I asked for _____ for Christmas, instead I got a random smart watch."
# If we're running THIS FILE using pysthon
if __name__ == "__main__":
    main()