# Runestone Academy: How To Think Like A Computer Scientist
# Chapter 4.11 Exercises
# Exercise 6

# Write a program that asks the user for the number of sides,
# the length of the side,
# the color,
# and the fill color of a regular polygon.
# The program should draw the polygon and then fill it in.

import turtle

sides = int(input('How many sides to your polygon? '))
length = int(input('How pixels long do you want the sides? '))
color = input('What color do you want the sides to be? ')
fill = input('What color do you want to fill the polygon? ')
degrees = 360 / sides

window = turtle.Screen()
window.bgcolor('orange')

pen = turtle.Turtle()
pen.color(color)

pen.begin_fill()
for i in range(sides):
    pen.forward(length)
    pen.right(degrees)

pen.fillcolor(fill)
pen.end_fill()
turtle.done()
