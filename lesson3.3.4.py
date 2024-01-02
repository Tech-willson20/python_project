import turtle
t = turtle.Turtle()
t.color("cyan")

for side in range(30):
    t.forward(side*20)
    t.right(120)

def mom():
    t = turtle.Turtle()
    t.color("cyan")
    for n in range(100):
        t.forward(n)
        t.right(20)
mom()



def spiral(sides, turn, color, width):
    t = turtle.Turtle()
    t.color(color)
    t.width(width)
    for n in range(sides):
        t.forward(n)
        t.right(turn)

spiral(50,60,"red",2)
for square in range(80):
    draw_square()
    jack.forward(5)
    jack.left(5)

