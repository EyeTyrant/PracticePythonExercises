# Runestone Academy: How To Think Like A Computer Scientist
# Chapter 4.11 Exercises
# Exercise 5

# Use for loops to make a turtle draw these regular polygons (regular means all sides the same lengths, all angles the same):
# An equilateral triangle
# A square
# A hexagon(six sides)
# An octagon(eight sides)

import turtle
wind = turtle.Screen()
wind.bgcolor('blue')

tri = turtle.Turtle()
tri.color('red')
tri.pensize(20)
tri.up()
tri.forward(50)
tri.down()

square = turtle.Turtle()
square.color('green')
square.pensize(15)
square.up()
square.forward(50)
square.down()

hexa = turtle.Turtle()
hexa.color('yellow')
hexa.pensize(20)
hexa.up()
hexa.left(180)
hexa.forward(50)
hexa.down()

octa = turtle.Turtle()
octa.color('orange')
octa.pensize(15)
octa.up()
octa.right(180)
octa.forward(50)
octa.down()

for i in range(3):
    tri.forward(150)
    tri.left(120)

for i in range(4):
    square.forward(150)
    square.right(90)

for i in range(6):
    hexa.forward(150)
    hexa.right(60)

for i in range(8):
    octa.forward(100)
    octa.left(45)
