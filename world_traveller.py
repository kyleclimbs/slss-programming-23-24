# Mcdonalds order
# Kyle Li
# November 3 2023
print("What's your name?")

name = input()

print(f"Nice to meet you,{name}!")

# list of questions
questions = [
    "Have you been to Asia?",
    "Europe",
    "Australia",
    "North America",
    "South America"
]

continent_count = 0

# For every question in the list
for question in questions:
    # Ask the question
    print(question)

    # get the user's answer (yes/no)
    visit_continent = input()

    # if the user's answer is yes
    if visit_continent.lower() == "yes":
        continent_count += 1

# Print out how many continents they've visited
print(f"You've been to {continent_count} / 7 continents!")

# final_score = 0



#     rating = int(input().strip(",.?!"))
#     final_score += rating

# print("Have you been to Asia?")
# visit_continent= input().strip(",.?!"). lover()

# print("Have you been to Europe?")
# visit_continent= input().strip(",.?!"). lover()

# print("Have you been to Australia?")
# visit_continent= input().strip(",.?!"). lover()

# print("Have you been to North America?")
# visit_continent= input().strip(",.?!"). lover()

# print("Have you been to South America?")
# visit_continent= input().strip(",.?!"). lover()

