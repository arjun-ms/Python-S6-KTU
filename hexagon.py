import turtle

t = turtle.Turtle()

# t.shape("turtle")
# t.screen.bgcolor("yellow")
t.fillcolor('red')
t.begin_fill()
for i in range(6):
    t.forward(100)
    t.right(60)
t.end_fill()


turtle.done()