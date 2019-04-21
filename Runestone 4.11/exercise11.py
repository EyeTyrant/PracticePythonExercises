# Runestone Academy: How To Think Like A Computer Scientist
# Chapter 4.11 Exercises
# Exercise 11

# Write a program to draw some kind of picture.
# Be creative and experiment with the turtle methods provided in Summary of Turtle Methods.

# Throws following Error when run on Runestone website but works on my computer:
# AttributeError: 'Turtle' object has no attribute 'shapesize' on line 26
# Maybe because the website confines attributes to the ones listed in the Summary.

import turtle

window = turtle.Screen()
window.bgcolor('blue')

head = turtle.Turtle()
head.speed(0)
head.color('yellow')
head.up()
head.left(90)
head.forward(200)
head.left(90)
head.down()
head.begin_fill()
head.circle(200)
head.fillcolor('yellow')
head.end_fill()
head.ht()

leye = turtle.Turtle()
leye.shape('circle')
leye.up()
leye.left(145)
leye.forward(100)
leye.right(55)
leye.shapesize(2, 4)
# leye.fillcolor('black')

reye = turtle.Turtle()
reye.shape('circle')
reye.up()
reye.left(35)
reye.forward(100)
reye.left(55)
reye.shapesize(2, 4)

mouth = turtle.Turtle()
mouth.speed(0)
mouth.shape('circle')
mouth.pensize(15)
mouth.up()
mouth.goto(-97, -70)
mouth.setheading(-60)
# mouth.right(135)
# mouth.forward(100)
# mouth.left(45)
mouth.down()
mouth.circle(120, 120)
mouth.left(70)
mouth.forward(-5)
mouth.shapesize(1, 2)
mouth.stamp()
mouth.up()
mouth.ht()
mouth.goto(-97, -70)
mouth. right(90)
mouth.forward(-5)
mouth.st()
mouth.stamp()

turtle.done()
