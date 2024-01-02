import turtle

rainbow = ["red", "orange", "yellow", "green", "blue", "purple"]
will=turtle.Turtle()

# Write whatever code you want here!
for lll in range(0,6):
    will.color(rainbow[lll])
    will.forward(50)
    for lo in range(1):
        will.right(90)
        will.penup()
        will.forward(5)
        will.pendown()
    

 
    
    
    