import turtle
window=turtle.Screen()
window.bgcolor("pink")
window.title("Infinity")
arrow=turtle.Turtle()
size=0
while True:
    for i in range(4):
        arrow.forward(size+1)
        arrow.left(90)
        size=size-5
    size=size+1