import turtle

t = turtle.Turtle()

t.width(5)
t.pencolor("red")
t.fillcolor("blue")

t.begin_fill()
for i in range(6):
    t.forward(100)
    t.left(60)
t.end_fill()

turtle.done()