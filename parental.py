# Kyle Li
# November 17 2023

questions =  ["Did you eat?", "Did you clean your room?", "Did you take out the trash?", "Did you do the laundry?"]
count = 0

for questions in questions:
        if input(questions) == "yes":
                count += 1

if  count == 0:
    print("You are gonna get it!")

elif count >= 1 and count <= 2:
       print("Okay...")

else:
       print("Thank you")