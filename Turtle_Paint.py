from turtle import Turtle, Screen

def draw_square(color):
    ti.pendown()
    ti.color('gray', color)
    ti.begin_fill()
    for _ in range(4):
        ti.forward(40)
        ti.left(90)
    ti.end_fill()
    ti.penup()

def draw_symbol(symbol, indent):
    ti.forward(indent)
    ti.pendown()
    ti.color('gray')
    ti.write(symbol, font=('Arial', 12, 'normal'))
    ti.penup()

def circle_t(size):
    ti.pendown()
    ti.begin_fill()
    ti.color('gray')
    ti.circle(size)
    ti.end_fill()
    ti.penup()

ti = Turtle()
ti.penup()
ti.speed(0)

# Background
indent = 20
ti.goto(-200, 80)
draw_symbol('Background', 5)
ti.goto(-200, 30)
draw_square('black')
draw_symbol('N', -20)
ti.goto(-200, -20)
draw_square('white')
draw_symbol('D', -20)

# Palette elements
y = 180
indent = 42
ti.goto(-190, y)
draw_square('red')
draw_symbol('R', indent)
ti.goto(-130, y)
draw_square('orange')
draw_symbol('O', indent)
ti.goto(-70, y)
draw_square('yellow')
draw_symbol('Y', indent)
ti.goto(-10, y)
draw_square('green')
draw_symbol('G', indent)
ti.goto(50, y)
draw_square('light blue')
draw_symbol('L', indent)
ti.goto(110, y)
draw_square('blue')
draw_symbol('B', indent)
ti.goto(170, y)
draw_square('violet')
draw_symbol('V', indent)

# Pen thickness
x = 200
y = 150
indent = 30
ti.goto(x, 140)
circle_t(5)
draw_symbol('1', indent)
ti.goto(x, 100)
circle_t(10)
draw_symbol('2', indent)
ti.goto(x, 53)
circle_t(15)
draw_symbol('3', indent)
ti.goto(x, 0)
circle_t(20)
draw_symbol('4', indent)
ti.goto(x, -60)
circle_t(25)
draw_symbol('5', indent)

print('Move down, up, right, left using the keyboard arrows.')
ti.hideturtle()

# THE MAIN PROGRAM
scr = Screen()
scr.bgcolor('white')
t = Turtle()
t.color('black')
t.width(5)
t.shape('circle')
t.pendown()
t.speed(0)

def draw(x, y):
    t.goto(x, y)

def move(x, y):
    t.pendown()
    t.goto(x, y)
    t.penup()

def setRed():
    t.color('red')

def setGreen():
    t.color('green')

def setBlue():
    t.color('blue')

def setOrange():
    t.color('orange')

def setYellow():
    t.color('yellow')

def setLightBlue():
    t.color('light blue')

def setViolet():
    t.color('violet')

def setWidth_1():
    t.width(5)

def setWidth_2():
    t.width(10)

def setWidth_3():
    t.width(25)

def setWidth_4():
    t.width(35)
def setWidth_5():
    t.width(35)
step=10
def stepUp():
    t.goto(t.xcor(), t.ycor() + step)

def stepDown():
    t.goto(t.xcor(), t.ycor() - step)

def stepLeft():
    t.goto(t.xcor() - step, t.ycor())

def stepRight():
    t.goto(t.xcor() + step, t.ycor())

def startFill():
    t.begin_fill()

def endFill():
    t.end_fill()

def background_black():
    scr.bgcolor('black')

def background_white():
    scr.bgcolor('white')

t.ondrag(draw)


scr.onscreenclick(move)
scr.onkey(setRed, 'r')
scr.onkey(setGreen, 'g')
scr.onkey(setBlue, 'b')
scr.onkey(setOrange, 'o')
scr.onkey(setYellow, 'y')
scr.onkey(setLightBlue, 'l')
scr.onkey(setViolet, 'v')

scr.onkey(setWidth_1, '1')
scr.onkey(setWidth_2, '2')
scr.onkey(setWidth_3, '3')
scr.onkey(setWidth_4, '4')
scr.onkey(setWidth_5, '5')

scr.onkey(stepUp, 'Up')
scr.onkey(stepDown, 'Down')
scr.onkey(stepLeft, 'Left')
scr.onkey(stepRight, 'Right')

scr.onkey(startFill, 'f')
scr.onkey(endFill, 'e')

scr.onkey(background_black, 'n')
scr.onkey(background_white, 'd')

scr.listen()
scr.mainloop()