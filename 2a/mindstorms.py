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

# Create four Turtle objects, to draw the three shapes
#turtle_sq = turtle.Turtle()
# turtle_cir = turtle.Turtle()
# turtle_tri = turtle.Turtle()
turtle_sig = turtle.Turtle()

# Change the Signature Turtles attributes
turtle_sig.shape("circle")
turtle_sig.color("#222222")
turtle_sig.speed(3)
turtle_sig.pensize(6)

# Code for previous sections --------------

# Change the Square Turtles attributes
#turtle_sq.shape("turtle")
#turtle_sq.color("#00FFFF")
#turtle_sq.speed(1)

# Move the Square Turtle somewhere remote
# turtle_sq.penup()
# turtle_sq.setpos(30,30)
# turtle_sq.pendown()

# Change the Circular Turtles attributes
#turtle_cir.shape("circle")
#turtle_cir.color("#000000")
#turtle_cir.speed(2)

# Move the Circular Turtle somewhere remote
#turtle_cir.penup()
#turtle_cir.setpos(-90,30)
#turtle_cir.pendown()

# Change the Triangular Turtles attributes
#turtle_tri.shape("arrow")
#turtle_tri.color("#11DDAA")
#turtle_tri.speed(3)

# Move the Triangular Turtle somewhere remote
#turtle_tri.penup()
#turtle_tri.setpos(-300,-120)
#turtle_tri.pendown()

# Call our square-drawing turtle function
#draw_square(turtle_sq)

# Call our square-drawing turtle function
#draw_circle(turtle_cir)

# Call our square-drawing turtle function
#draw_triangle(turtle_tri)

# Code for turtle mini-project section ----

# x and y turtle coordinated generated from http://willowsystems.github.io/jSignature

# Create array of x-cooridnates
x = [364,366,366,367,367,367,367,367,366,365,364,359,357,352,347,344,340,336,333,329,325,320,312,307,304,301,299,298,296,295,294,293,292,291,290,288,287,285,285,284,283,283,283,284,286,290,302,312,317,328,335,342,367,371,375,393,398,403,408,413,447,465,470,478,480,479,474,464,462,459,443,439,425,410,406,398,393,389,384,377,372,367,362,365,367,370,373,377,380,382,388,391,395,399,406,410,415,424,430,435,445,451,458,465,476,484,491,496,512,517,521,526,531,535,549,554,558,563,568,573,577,587,591,596,600,605,609,614,622,630,634,638,641,645,648,654,658,660,664,668,670,671,672,672,672,671,669,667,664,660,657,651,648,644,639,634,625,619,611,592,584,576,572,568,560,553,546,543,536,533,530,527,524,521,516,509,507,504,502,500,499,498,498,499,501,503,505,508,511,514,518,528,533,538]
# Create array of y-coordinates
y = [103,106,111,115,120,125,131,137,148,152,156,167,170,177,182,185,188,190,192,194,196,197,198,198,196,193,189,185,181,176,172,167,163,158,153,147,142,135,130,126,122,116,110,105,102,97,90,87,85,82,80,79,73,72,71,69,68,67,67,66,65,65,65,69,78,83,94,109,112,116,132,136,145,151,153,155,157,158,159,160,160,161,161,159,162,164,166,171,173,176,180,183,185,187,191,193,195,197,198,198,199,199,199,199,199,198,197,197,193,192,191,190,189,188,184,182,181,180,178,177,175,173,171,170,168,166,165,162,159,155,153,151,149,147,145,140,136,133,128,120,117,111,105,93,86,80,74,71,66,60,56,50,48,45,42,40,37,36,35,35,36,37,38,39,42,45,48,50,54,56,58,61,63,65,70,79,82,88,94,97,102,108,113,120,124,127,130,132,135,137,139,141,141,140]

# Shift values, to get the signature as centered as possible.
shift_x = -500
shift_y = 150

# Move turtle to first (x,y) pair
turtle_sig.penup()
turtle_sig.setpos(364 + shift_x,-103 + shift_y )
turtle_sig.pendown()

# Have turtle move to respective (x,y) pairs with a for loop

for index in range(len(x)):
    turtle_sig.setx(x[index]+shift_x)
    # Invert y coordinates to orient image correctly
    turtle_sig.sety(-y[index]+shift_y)

# Create an exit condition
window.exitonclick()
