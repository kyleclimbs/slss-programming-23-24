# Bubble tea popularity algorithm
# Author Kyle
# October 27 2023

# Ask 5 users what their favourite bubble tea place is
# Prints out summary of the data

NUM_RESPONDENTS = 5 

# like counters
coco_likes = 0    # initialize the variable tot 0
suntea_likes = 0
chatime_likes = 0
bubqueen_likes = 0

# Ask the user what their favourite bubble tea place is
# store the info somewhere
for _ in range(NUM_RESPONDENTS):
    print("What's your favourite bubblle tea place?")

    fave_place = input().strip(",.?!").lower()

    if fave_place == "coco":
        coco_likes = coco_likes + 1
    elif fave_place == "suntea":
        suntea_likes += 1 
    elif fave_place == "chatime":
        chatime_likes += 1 
    elif fave_place == "bubqueen":
        bubqueen_likes += 1 

#  Print out a summary of all the places
#GIve the raw score and the percentage
print(f'CoCo likes: {coco_likes}')
print(f'suntea: {suntea_likes}')
print(f'chatime likes: {chatime_likes}')
print(f'bubqueen likes: {bubqueen_likes}')

# Tally or counting algo
# options: CoCo, Suntea, Chatime, Bubble Queen
# if they choose any of these options, increase the counter
 
print(f"CoCo percentage: {coco_likes / NUM_RESPONDENTS * 100}%")

print(f"Bubble queen likes: {bubqueen_likes / NUM_RESPONDENTS * 100}%")

print(f"Suntea likes: {suntea_likes / NUM_RESPONDENTS * 100}%")

print(f"Chatime likes: {chatime_likes / NUM_RESPONDENTS * 100}%")