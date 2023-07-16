import turtle

t = turtle.Turtle()

side_length = 100

angle = 72

for i in range(5):
    t.forward(side_length)
    t.left(angle)
    
turtle.done()