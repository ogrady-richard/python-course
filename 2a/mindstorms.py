## @package mindstorms
#  \brief     Programming Foundations with Python - 2A
#  \details \n This .py package is for the turtle functions of the first project of 'Programming Foundations with Python'.
#  \author    Richard O'Grady
#  \version   0.2
#  \date      April, 2015
#  \copyright GNU Public License.

# Import the turtle package
import turtle

# Functions -------------------------------

## Draw Square with Turtle
# @brief Draw a square, anchored at the top-left corner (due south-west of the turtles origin.)
# @param turtleID The name of the turtle that is drawing the square
def draw_square(turtleID):
    # Tell the Turtle object to draw a square below and to the right of it's origin.
    for x in range(0,4):
        turtleID.forward(100)
        turtleID.right(90)

## Draw Circle with Turtle
# @brief Draw a circle anchored above the turtle
# @param turtleID The name of the turtle that is drawing the circle
def draw_circle(turtleID):
    #Tell the Turtle object to draw a circle above its origin
    turtleID.circle(90)

## Draw Triangle with Turtle
# @brief Draw a triangle anchored at its bottom-left vertex
# @param turtleID The name of the turtle that is drawing the triangle
def draw_triangle(turtleID):
    #Tell the Turtle object to draw a triangle to the right of it's origin
    for x in range(0,3):
        turtleID.forward(100)
        turtleID.left(180-60)
    
# Main ------------------------------------

# Create a window object, and color it red.
window = turtle.Screen()
window.bgcolor("red")

# Create three Turtle objects, to draw the three shapes
turtle_sq = turtle.Turtle()
turtle_cir = turtle.Turtle()
turtle_tri = turtle.Turtle()

# Change the Square Turtles attributes
turtle_sq.shape("turtle")
turtle_sq.color("#00FFFF")
turtle_sq.speed(1)

# Move the Square Turtle somewhere remote
turtle_sq.penup()
turtle_sq.setpos(30,30)
turtle_sq.pendown()

# Change the Circular Turtles attributes
turtle_cir.shape("circle")
turtle_cir.color("#000000")
turtle_cir.speed(2)

# Move the Circular Turtle somewhere remote
turtle_cir.penup()
turtle_cir.setpos(-90,30)
turtle_cir.pendown()

# Change the Triangular Turtles attributes
turtle_tri.shape("arrow")
turtle_tri.color("#11DDAA")
turtle_tri.speed(3)

# Move the Triangular Turtle somewhere remote
turtle_tri.penup()
turtle_tri.setpos(-300,-120)
turtle_tri.pendown()

# Call our square-drawing turtle function
draw_square(turtle_sq)

# Call our square-drawing turtle function
draw_circle(turtle_cir)

# Call our square-drawing turtle function
draw_triangle(turtle_tri)

# Create an exit condition
window.exitonclick()
