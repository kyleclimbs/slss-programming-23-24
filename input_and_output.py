# Input and Output 
# Author: Kyle
# Date: 19 September 2023

import random
import time

# Output a quote from someone famous
print("Git is Google drive on caffiene by Ubial")
print("I can climb higher than you - kyle._climbs")

print("input is vital, --Ubial")

# Ask a question to the user
input("What's your favourite food? ")
# Respond with what a human would say
print("MMmmmmmmmmmmmm. That is so delicious.")

# Ask a question to the user running our app
favourite_food = input("what is your favourite food?")

# Respond with something a human would say
print(f"Ooooooooo, {favourite_food} sounds so good")



# If their favourite food is sushi, reply with yum.
# Make a comment about their favourite food but NOT BE OVERLY REPETITIVE
# Create a list of possible responses
list_of_food_responses = [
    f"Oh, I've never had {favourite_food} before.",
    "Mmmm. That sounds good!",
    "I heard that that is delicious.",
    "Cool."
 ]
# Choose one of those responses randomly
random_food_response = random.choice(list_of_food_responses)
# Print out that chosen response
print(random_food_response)
 
 # If their favourite food is sushi, reply with yum.
if favourite_food == "sushi":
    print("Yum! 2")
    print("I love sushi!.. I think!")
elif favourite_food == "Burgers":
    print("Mmmm. I love burgers.")
else:
    # Make a comment about their favourite food but NOT OVERLY REPETITIVE
    # Create a list of possible responses
    list_of_food_responses = [
    "Oh, I've never had {favourite_food} before!",
    "Mmmmm. That sounds good!",
    "I heard that that is very good!",
    "That's cool!",
    "Oh! that does sound pretty good right about now!"
    ]

    # Choose one of those responses randomly
    random_food_responses = random.choice(list_of_food_responses)

    time.sleep(1)

    # Print out those responses randomly
    print(random_food_response)