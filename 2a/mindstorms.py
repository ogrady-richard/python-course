## @package mindstorms
#  \brief     Programming Foundations with Python - 2A
#  \details \n This .py package is for the turtle functions of the first project of 'Programming Foundations with Python'.
#  \author    Richard O'Grady
#  \version   0.1
#  \date      April, 2015
#  \copyright GNU Public License.




# Import the turtle package
import turtle

# Functions -------------------------------

## Draw Square with Turtle
# @brief Draw a square, anchored at the top-left corner (due south-west of the turtles origin.)
def draw_square():

    # Tell the Turtle object to draw a square below and to the right of it's origin.
    turtle_obj.forward(100)
    turtle_obj.right(90)
    turtle_obj.forward(100)
    turtle_obj.right(90)
    turtle_obj.forward(100)
    turtle_obj.right(90)
    turtle_obj.forward(100)
    turtle_obj.right(90)

# Main ------------------------------------

# Create a window object, and color it red.
window = turtle.Screen()
window.bgcolor("red")

# Create a Turtle object
turtle_obj = turtle.Turtle()

# Call our new square-drawing turtle function
draw_square()

# Create an exit condition
window.exitonclick()
