# Runestone Academy: How To Think Like A Computer Scientist
# Chapter 4.11 Exercises
# Exercise 10

# Write a program to draw a face of a clock that looks something like this:

import turtle

window = turtle.Screen()
window.bgcolor('lightgreen')
pen = turtle.Turtle()
pen.color('blue')
pen.shape('turtle')
pen.pensize(3)
pen.left(90)

x = 0
while x < 12:
    pen.up()
    pen.forward(100)
    pen.down()
    pen.forward(20)
    pen.up()
    pen.forward(15)
    pen.stamp()
    pen.forward(-135)
    pen.right(30)
    x += 1

pen.right(90)
turtle.done()
