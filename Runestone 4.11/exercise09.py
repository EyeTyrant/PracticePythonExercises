# Runestone Academy: How To Think Like A Computer Scientist
# Chapter 4.11 Exercises
# Exercise 9

# Write a program to draw a shape like this: (pentagram)

import turtle

window = turtle.Screen()
pen = turtle.Turtle()
pen.speed(1)
pen.right(108)
x = 0
while x < 5:
    pen.forward(100)
    pen.left(144)
    x += 1

turtle.done()
