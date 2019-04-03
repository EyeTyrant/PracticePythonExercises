# Runestone Academy: How To Think Like A Computer Scientist
# Chapter 2.13 Exercises
# Exercise 3

# Ask the user for the time now (in hours),
# and then ask for the number of hours to wait for the alarm.
# Your program should output what the time will be on the clock when the alarm goes off.

now = int(input("Enter hour: "))
alarm = int(input("How many hours until alarm: "))

print((now + alarm) % 24)
