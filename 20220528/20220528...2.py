import turtle


def tree(x, y):
    turtle.penup
    turtle.goto(x, y)
    turtle.color("green")
    turtle.pendown()
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(150)
    turtle.right(60)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.right(60)
    turtle.forward(50)
    turtle.left(120)
    turtle.forward(50)
    turtle.right(60)
    turtle.forward(50)
    turtle.left(120)
    turtle.forward(50)
    turtle.right(60)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.right(60)
    turtle.forward(150)
    turtle.left(120)
    turtle.forward(100)
    turtle.end_fill('green')


tree(0, 0)
turtle.done