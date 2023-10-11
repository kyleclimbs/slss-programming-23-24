# Food Suggestion Bot
# Author: Kyle
# 6 Ocotber 2023

# A bot that asks the user what their favourite food is. Based on that food, it will classify the type/genre/cuisine of the food,
# then give a restaurant suggestion.

import random
import time

# Introduce the bot to the user
# Ask the user what their favourite food is
print("Hello, I am here to suggest you a restaurant")
time.sleep(1)
fave_food = input("To help me suggest a restarant, tell me what your favourite food is")
time.sleep(1)

# Italian Cuisine
italian_food = ["pasta", "pizza", "canneloni", "tiramisu"]
# Indian Cuisine
indian_food = ["butter chicken", "chicken biryiani", "chicken tiki masala"]

# If they answer with Italian food, suggest an Italian restaurant
if fave_food.lower().strip("!.,?") in italian_food:
    print("I see that you might like Italin food")
    time.sleep(1)
    print("I suggest Broli Kitchen.")
    time.sleep(1)
    print("Here's their address.")
    print("186-8180 No 2 Road, Richmond, BC")
elif fave_food.lower().strip("!.,?") in indian_food:
    print("I see that you might like Indian food!")
    time.sleep(1)
    print("I suggest Ginger Indian Cuisine.")
    time.sleep(1)
    print("Here's their address.")
    print("9100 Blundell Road, Richmond, BC") 
else:
    print("Sorry, I'm not sure what kind of food that is.")
    time.sleep(1)
    print("I can't, unfortuately provide a suggestion.")








