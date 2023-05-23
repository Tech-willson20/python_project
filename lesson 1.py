# Drawing shape with turtle
import turtle
def shape_triangle():
    fred = turtle.Turtle()
    fred.color("red")
    fred.forward(100)
    fred.right(135)
    fred.forward(140)
    fred.right(135)
    fred.forward(100)

def shape_square():
    import turtle
    fred = turtle.Turtle()
    fred.color("green")
    fred.forward(100)
    fred.right(90)
    fred.forward(100)
    fred.right(90)
    fred.forward(100)
    fred.right(90)
    fred.forward(100)

def shape_trapl():
    # Drawing shape with turtle
    fred = turtle.Turtle()
    fred.color("red")
    fred.backward(100)
    fred.right(135)
    fred.forward(140)
    fred.left(135)
    fred.forward(200)


    

shape_square()
shape_triangle()
shape_trapl()