from turtle import *

offset_x = -500

offset_y = 300

data = []

for i in open("dots.txt"):
    data.append(i.strip().split(" "))
    
x0, y0 = int(data[0][0]), int(data[0][1])

penup()

goto(x0 + offset_x, - y0 + offset_y)

pendown()

for x in range(len(data)):
    x1, y1 = int(data[x][0]) + offset_x, -int(data[x][1]) + offset_y
    goto(x1,y1)

update()

exitonclick()
