import turtle
turtle.Screen().bgcolor("Pink")
turtle.Screen().setup(400,500)
arrow=turtle.Turtle()
num_sides= 8
for i in range(num_sides):
    arrow.forward(150)
    arrow.right(90)
turtle.done()