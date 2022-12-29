from turtle import *
data = []
for i in open("dots.txt"):
    data.append(i.strip().split(" "))
x0, y0 = int(data[0][0]), int(data[0][1])
penup()
goto(x0,y0)
pendown()
for x in range(len(data)):
        x1,y1 = int(data[x][0]), int(data[x][1])
        goto(x1,y1)
update()
exitonclick()
