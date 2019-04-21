# Runestone Academy: How To Think Like A Computer Scientist
# Chapter 4.11 Exercises
# Exercise 13

# A sprite is a simple spider shaped thing with n legs coming out from a center point.
# The angle between each leg is 360 / n degrees.
# Write a program to draw a sprite where the number of legs is provided by the user.

import turtle

legs = int(input('How many legs on your spider? '))
angle = 360 / int(legs)

pen = turtle.Turtle()
pen.pensize(6)
pen.dot(40)

for i in range(legs):
    pen.forward(75)
    pen.forward(-75)
    pen.left(angle)

pen.ht()
turtle.done()
