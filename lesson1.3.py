import turtle
import time
amy = turtle.Turtle()
amy.color("green")
amy.fillcolor("red")
amy.begin_fill()
for side in [1, 2, 3, 4,5,6]:
    amy.forward(100)
    amy.right(60)
    time.sleep(0.5)
amy.end_fill()
def cll():
     # create a turtle object
    t = turtle.Turtle()

    # set the fill color
    t.fillcolor("green")

    # begin filling the background
    t.begin_fill()

    # draw the triangle
    for i in range(3):
        t.forward(100)
        t.left(120)

    # end filling the background
    t.end_fill()

    # exit on click
    turtle.exitonclick()
  
cll()