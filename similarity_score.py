# comparing similarity scores
# Kyle Li
# NOvember 8 2023

# calculate similarity scores between 2 people

# Create two lists that represent the movies that people like
ubials_favourite_movies = [
    "The Matrix",
    "Avengers: Endgame",
    "The Empire Strikes Back",
    "Infernal Affairs",
    "Rougue one",
]

bens_favourite_movies = [
    "Thomas The Train",
    "Infernal Affairs",
    "Rougue one",
    "Guarduans of the galaxy Vol 3",
]

# Initiailze the similarity score
similarity_score = 0 

# For each item in the first list
for movie in ubials_favourite_movies:
    # If that item is in the second list
    for movie in bens_favourite_movies:
        # Increase the similarity score by 1
        similarity_score += 1

# Display the results
print(f"Ubial and Ben have a similarity score of: {similarity_score}")