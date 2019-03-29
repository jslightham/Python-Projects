import turtle             
wn = turtle.Screen()
t = turtle.Turtle()
t.speed('fastest')
t.left(90)
t.back(150)
def draw(l):
    if(l < 1):
        return;
    else:
        t.forward(l)
        t.right(30)
        draw(l/1.5)
        t.left(60)
        draw(l/1.5)
        t.right(30)
        t.backward(l)

draw(125);
