from turtle import*
bgcolor("purple")

#step 1:draw a square
speed(7)
width(9)
color("black")

forward(200)
left(90)

forward(200)
left(90)
forward(200)
left(90)

forward(200)
left(90)
forward(70)

#end of square
#drawing a door
color("green")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()
#roof
left(180)
left(30)
forward(200)
left(120)
forward(200)
penup()

goto(180,180)

pendown()
left(60)
left(30)
shape("turtle")
right(60)
forward(35)
right(90)
forward(35)
right(90)
forward(35)
right(90)
forward(35)
right(90)
goto()

exitonclick()


