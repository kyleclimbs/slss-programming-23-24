---
tags:
  - notes 
  - natural-language-processing 
  - 2023-2024
  - programming-level-1-2
---
# Natural Language Processing

## Output
We can use a function to display text and symbols to the screen.
We use the `print` function to display the output.

```Python 
print("your text goes here")
```

# Headers

## Comments
Comments are pieces of text that are not interpreted by python.
This means the text is ignored.
We use the # symbol to make comments.




# Input

We can grab info from the user using the input function. 
When we run the function, it does two things: 
1. It waits for the user to write something or nothing
2. The user presses Enter/Return to indicate that they're finished

```python 
input()

input(<prompt>)   # prints out the prompt then waits

```

# Variables
Variables allow us to store information for the time that our app is running

```python 
favourite_food = input("what is your favourite food?")

```
favourite_food -> name of the variable
= -> assignment operator 
input...->value

# [[Strings]]

# Format strings
If we want to evaluate inside of a string, we use *f-strings

```python
fave_food = input("what is your favourite food?")

print(f"Oooooooooo, {fave_food} sounds so yummy!)
```