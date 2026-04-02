from turtle import *
from time import sleep
 
t = Turtle()
 
def ir(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
 
def planocart():
    t.speed(0)
    #eixo x
    ir(-300, 0)
    t.goto(300, 0)
    t.stamp()
    #eixo y
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
    if x != 0:
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
y_inicio = func1(-200)
if y_inicio is not None:
    ir(-200, y_inicio)
for x in range(-99, 101):
    y = func1(x)
    if y is not None:
        t.goto(x, y)

sleep(3)
t.clear()
planocart()

y_inicio = func2(-200)
if y_inicio is not None:
    ir(-200, y_inicio)
for x in range(-99, 101):
    y = func2(x)
    if y is not None:
        t.goto(x, y)

sleep(3)
t.clear()
planocart()

ir(-200, func3(-200))
for x in range(-99, 101):
    t.goto(x, func3(x))

sleep(3)
t.clear()
planocart()

ir(-200, func4(-200))
for x in range(-99, 101):
    t.goto(x, func4(x))

sleep(3)
t.clear()
planocart()

ir(-200, func5(-200))
for x in range(-99, 101):
    t.goto(x, func5(x))

sleep(3)
t.clear()
planocart()

ir(-200, func6(-200))
for x in range(-99, 101):
    t.goto(x, func6(x))
 
mainloop()