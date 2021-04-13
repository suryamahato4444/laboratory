import turtle
screen=turtle.Screen()
    # pen.circle(r)
pen=turtle.Turtle()
def drawCircle(x,y,r):
    pen.penup()
    pen.goto(x,y-r)
    pen.pendown()
    pen.circle(r)
drawCircle(0,0,200)
    # pen.pendown()
def makepicture(r):
    if r<20:
        pass
    else:
        drawCircle(0,0,r)
        makepicture(r-20)
makepicture(100)
for i in range(100,100):
    drawCircle(0,0,i)
# turtle

turtle.done()