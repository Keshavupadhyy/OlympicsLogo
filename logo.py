import turtle
def draw_ring(colo: object, x: object, y: object) -> object:
    turtle.penup()
    turtle.color(turtle.color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(50)

turtle.speed(5)
turtle.write(5)
draw_ring("blue", -120,0)
draw_ring("black", 0,0)
draw_ring("red", 120,0)
draw_ring("yellow", -60, -50)
draw_ring("green", 60, -50)
turtle.hideturtle()
turtle.done()
