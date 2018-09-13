import turtle             
wn = turtle.Screen()        
t = turtle.Turtle()
t.left(90)
t.back(50)
def draw(l):
    if(l < 1):
        return;
    else:
        t.forward(l)
        t.right(30)
        draw(l-15)
        t.left(60)
        draw(l-15)
        t.right(30)
        t.backward(l)

draw(100);
