# Runestone Academy: How To Think Like A Computer Scientist
# Chapter 4.11 Exercises
# Exercise 4

# Assume you have a list of numbers 12, 10, 32, 3, 66, 17, 42, 99, 20.
# Write a loop that prints each of the numbers on a new line.
# Write a loop that prints each number and its square on a new line.

# a.

import math
nums = [12, 10, 32, 3, 66, 17, 42, 99, 20]
for num in nums:
    print(num)

# b.
for num in nums:
    print(num, 'and it\'s square root is', math.sqrt(num))
