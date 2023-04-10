#my house
from turtle import *
bgcolor("green")
speed(30)
width(7)
#step 1:draw a square
color("purple")
begin_fill()

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
forward(70)
end_fill()
# end of square


# drawing a door
color("red")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()



penup()
goto(200, 200)
pendown()


#roof
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
right(60)
color("black")

penup()
goto(180,180)
pendown()

#window
color("blue")
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

color("yellow")
width(7)
penup()
goto(20,180)
pendown()
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)











exitonclick()
