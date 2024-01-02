import turtle
amy = turtle.Turtle()

# Make the width thicker so that the line will be easier to see
amy.width(5)
r=["red","orange","yellow"]
for col in range(0,3):
    amy.color(r[col])
    amy.pendown()
    amy.forward(50)
    amy.penup()
    amy.forward(10)
