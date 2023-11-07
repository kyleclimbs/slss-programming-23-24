# Semester evaluater
# Kyle li
# November 6 2023
current_courses = input("How many courses are you taking this semester?")

NUMS_RESPONDENDTS = current_courses

course_num = 1 

sum = 0

for i in range(int (NUMS_RESPONDENDTS) ):
    course_evaluation = input ("What would you rate course" + str(i +1) + " out of 5?")
    sum += int(course_evaluation)
    course_average = sum / int (NUMS_RESPONDENDTS)
if course_average <=1:
    print("Ouch")
elif course_average > 1 and course_average < 3:
    print ("Not a bad semester")
else:
    print("Glad to hear that!")