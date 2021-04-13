import turtle
screen=turtle.Screen()
# pen.turtle()
# pen.forward(200)
# pen.left(90)
# pen.forward(200)
# pen.left(90)
# pen.forward(200)
# pen.left(90)
# pen.forward(200)
# pen.left(90)



pen=turtle.Turtle()
pen.fillcolor('yellow')
sides=6
length=100
angle=360//sides
for i in range(sides):
    pen.forward(200)
    pen.right(angle)
    # pen.fillcolor('yellow')
turtle.done()

