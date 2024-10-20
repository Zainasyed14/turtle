import turtle
turtle.Screen().bgcolor("pink")
turtle.Screen().setup(400,500)
arrow=turtle.Turtle()
num_sides=8
for i in range(num_sides):
    arrow.forward(90)
    arrow.right(60)
turtle.done()