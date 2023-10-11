# Loop practice
# Author: Kyle Li
# Date: 10 October 2023

import time

# create a list of groceries
groceries = ["hot wheels", "lego", "ice cream",]

# Do something for each thing on the list
# Print it out in a pretty way
#   e.g.
#   * hotwheels
#   ---
#   * lego
#   ---
#   etc.

# print(f"* {groceries[0]")
# print(f"---)
# print(f"* {groceries[1]")
# print(f"---)
# print(f"* {groceries[2]")
# print(f"---)

for item in groceries :
    print(f"* {item}")
    print(" ---")

# Using the above method, create the thing below:
# *
# **
# ***
# ****
# *****
# ******

pyramid = ["*", "**", "***", "****", "*****", "******"]

for items in pyramid:
    print(f"{items}")

# Problem:
# Create a New Years countdown that's automated
# Requirments:
#   - starts at 10
#   - counts down every second printing the second it's at 
#   - instead of reacting zero, it prints out "Happy New Year"
# Example Output
# 10
# 9
# 8
# ...
# 1 
# Happy New Year!

countdown = ["10", "9", "8", "7", "6", "5", "4", "3", "2", "1", "Happy New Years!!!"]
for item in countdown:
    print(f"{item}")
    time.sleep(1)
