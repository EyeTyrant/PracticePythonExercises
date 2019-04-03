# Runestone Academy: How To Think Like A Computer Scientist
# Chapter 2.13 Exercises
# Exercise 10

# Write a program that will compute MPG for a car.
# Prompt the user to enter the number of miles driven and the number of gallons used.
# Print a nice message with the answer.

m = int(input('Enter miles driven: '))
g = int(input('Enter gallons used: '))

print('Your miles per gallon is ' + str(m / g))
