# Star Wars 
# Author: Kyle Li
# Date: 16 October 2023

# Ask the user if they like red or capes
print("I will decide whether you are worthy of joining the dark side.")
like_red = input("Is red your colour of choice? ")
like_capes = input("Are capes your style? ")

# Give response based on inputs
if like_red.lower() == "yes":
    print(" And the rockets' red glare, the bombs bursting in air..I welcome you to the land of the  dark side.")
elif like_red.lower() == "no":
    if like_capes.lower() == "yes":
        print("Welcome to the darkness.")
    else:
        print("Begone light dweller.")
        print("You are too weak.")
else:
    print("You are not worthy. You are not welcome in dark side.")
    print("Begone light dweller.")