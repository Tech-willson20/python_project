import turtle
dizzy = turtle.Turtle()
dizzy.color("blue")
dizzy.width(5)

for length in range(0,500,10):
    dizzy.forward(length)
    dizzy.right(90)
