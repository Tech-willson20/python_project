import turtle
amy=turtle.Turtle()
colo=["red","orange","yellow","green"]
for sides in range(0,4):
    amy.color(colo[sides])
    amy.forward(100)
    amy.right(90)