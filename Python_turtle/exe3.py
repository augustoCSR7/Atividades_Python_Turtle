import turtle

turtle.shape('arrow')
turtle.bgcolor('black')
turtle.color('red')
turtle.pensize(2)
turtle.penup()
turtle.goto(0,-100)
turtle.pendown()

turtle.speed(10)

x = 10
call = x
while True:
    turtle.circle(call, 360, 100)
    call += 10
    if call > 300:
        break
turtle.done()