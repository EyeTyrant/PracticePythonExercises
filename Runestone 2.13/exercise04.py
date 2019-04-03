# Runestone Academy: How To Think Like A Computer Scientist
# Chapter 2.13 Exercises
# Exercise 4

# Write a general version of the program which asks for the starting day number,
# and the length of your stay,
# and it will tell you the number of day of the week you will return on.

departureDay = int(input('Departure day (day of week (0 - 6): '))
lengthOfStay = int(input('Length of stay (number of days): '))

print((departureDay + lengthOfStay) % 7)
