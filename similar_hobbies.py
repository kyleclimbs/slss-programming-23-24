# Kyle Li
# November 20 2023


hobbies1 = input("Enter hobbies for person 1: ")

hobbies2 = input("Enter hobbies for person 2: ")

list1 = hobbies1.lower().split()

list2 = hobbies2.lower().split()

common_interests = 0
    
for hobby in list1:
    if hobby in list2:
        common_interests += 1

print(f"You're similarity score!: {common_interests}")