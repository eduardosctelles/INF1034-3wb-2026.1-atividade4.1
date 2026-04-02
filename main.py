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

ir(0, func1(0))
for x in range(1, 300):
    t.goto(x, func1(x*100))

sleep(3)
t.clear()
t.right(90)
planocart()

ir(1, func2(x*0.001))
for x in range(2, 300):
    t.goto(x, func2(x)/1000)

sleep(3)
t.clear()
t.right(90)
planocart()

ir(-150, func3(-15))
for x in range(-14, 16):
    t.goto(x*10, func3(x))

sleep(3)
t.clear()
t.right(90)
planocart()

ir(-150, func4(-15))
for x in range(-14, 16):
    t.goto(x*10, func4(x))

sleep(3)
t.clear()
t.right(90)
planocart()

ir(-150, func5(-15))
for x in range(-14, 16):
    t.goto(x*10, func5(x))

sleep(3)
t.clear()
t.right(90)
planocart()

ir(-250, func6(-10))
for x in range(-9, 11):
    t.goto(x*25, func6(x))

mainloop()