from turtle import *
t = Turtle()

def ir(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def planocart():
    t.speed(0)
    #Eixo X
    ir(-300, 0)
    t.goto(300, 0)
    t.stamp()
    #Eixo Y
    ir(0, -300)
    t.goto(0, 300)
    t.setheading(90)
    t.stamp()
    t.speed(6)

def func1(x):
    if x >= 0:
        return x**0.5
    else:
        return None

def func2(x):
    if x > 0 or x <= -1:
        return 1 / x
    else:
        return None

def func3(x):
    return 2**x 

def func4(x):
    return 5 - x**2

def func5(x):
    return x**2 - 5*x + 6

def func6(x):
    return x**3 - x**2 - x + 1

planocart()

for x in range(-100, 101):
    t.goto(2*x, func1(2*x))

t.clear()
planocart()

for x in range(-100, 101):
    t.goto(2*x, func2(2*x))

t.clear()
planocart()

for x in range(-100, 101):
    t.goto(2*x, func3(2*x))

t.clear()
planocart()

for x in range(-100, 101):
    t.goto(2*x, func4(2*x))

t.clear()
planocart()

for x in range(-100, 101):
    t.goto(2*x, func5(2*x))

t.clear()
planocart()

for x in range(-100, 101):
    t.goto(2*x, func6(2*x))


mainloop()