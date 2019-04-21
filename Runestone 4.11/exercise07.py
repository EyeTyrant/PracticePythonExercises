# Runestone Academy: How To Think Like A Computer Scientist
# Chapter 4.11 Exercises
# Exercise 7

# A drunk pirate makes a random turn and then takes 100 steps forward, makes another random turn, takes another 100 steps, turns another random amount, etc. A social science student records the angle of each turn before the next 100 steps are taken. Her experimental data is 160, -43, 270, -97, -43, 200, -940, 17, -86. (Positive angles are counter-clockwise.) Use a turtle to draw the path taken by our drunk friend. After the pirate is done walking, print the current heading.

import turtle

steps = 100
turn = [160, -43, 270, -97, -43, 200, -940, 17, -86]

window = turtle.Screen()
window.bgcolor('tan')
pirate = turtle.Turtle()
pirate.pensize(5)
pirate.speed(1)

for i in turn:
    pirate.forward(steps)
    pirate.left(i)

print(pirate.heading())

turtle.done()
