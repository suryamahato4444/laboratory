from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    # right(12)
    left(270)
    if abs(pos()) < 2:
        break
end_fill()
done()