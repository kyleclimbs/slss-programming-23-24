# CHip Rater
# Kyle Li
# November 1 2023

# Interview people about their
# perception of how delicious chips are
# based on a set of questions

# In the end, we'll give an aggregate score.

# Greet the user
print("Please answer the following questions based on the chip that you just ate.")

# Create a list of questions to ask
questions = [
    "How crispy is the chip on a scale to 1 to 5? 5 is very crispy. 1 is very mushy",
    "How would you rate the taste from 1 to 5? 5 is the best taste ever. 1 is I would rather eat dirt.",
    "From 1 to 5, how would you rate the packaging? 5 is I would buy this JUST for the packaging. 1 would be someone was paid to pack this???"
]

final_score = 0

# Ask the questions to the user
for question in questions: 
    print(question)

    # Store their response
    rating = int(input().strip(",.?!"))
    final_score += rating
# Do some math
average_score = final_score / len(questions)
# Present the results to the user
print(f"The average score of this chip is: {average_score:.2f}/ 5")