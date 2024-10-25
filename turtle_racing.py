import turtle
import time
import random

WIDTH,HEIGHT=1000,500
COLORS=[
    "red", "green", "blue", "yellow", "cyan", "magenta", "black", "white", "gray", "orange",
    "purple", "pink", "brown", "lime", "olive", "navy", "teal", "maroon", "aqua", "fuchsia",
    "gold", "silver", "beige", "coral", "crimson", "indigo", "ivory", "khaki", "lavender", "moccasin",
    "orchid", "plum", "salmon", "sienna", "tan", "tomato", "turquoise", "violet", "wheat", "azure",
    "chocolate", "firebrick", "forestgreen", "gainsboro", "honeydew", "hotpink", "lightblue", "lightgreen", "lightpink", "lightsalmon"
]

def no_of_turtle():
    turtle=0
    while True:
        turtle=input("enter no. of turtles (2-50): ")
        if turtle.isdigit():
            turtle=int(turtle)
        else:
            print("enter the valid no. try again")
            continue
        if 2<=turtle<=50:
            return turtle
        else:
            print("enter no. between 2 to 50")

def init_turtle():
    screen=turtle.Screen()
    screen.bgpic(r"K:\code\python_projects\Tanjiro.gif")
    screen.setup(WIDTH,HEIGHT)
    screen.title("Racing Track")

def race(colors):

    turtles=create_turtle(colors)
    line()
    while True:
        for racer in turtles:
            distance=random.randint(1,20)
            racer.forward(distance)

            x,y=racer.pos()
            if y>=HEIGHT//2 - 30:
                return colors[turtles.index(racer)]

def line():
    a=turtle.Turtle()
    a.shape("triangle")
    a.shapesize(2,2,2)
    a.speed(5)
    a.penup()
    a.setpos(-(WIDTH//2),-198)
    a.pendown()
    a.pencolor("white")
    a.pensize(10)
    a.forward(WIDTH)

def create_turtle(colorss):
    turtles=[]
    x=-(WIDTH)/2+20
    increment=WIDTH/len(colorss) 
    for i,colr in enumerate(colorss):
        racer=turtle.Turtle()
        racer.color(colr)
        racer.speed(10)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(x,-220)
        racer.pendown()
        racer.speed("normal")
        turtles.append(racer)
        x+=increment

   
    return turtles

    
racers=no_of_turtle()

init_turtle()

random.shuffle(COLORS)
colorss=COLORS[:racers]


print("the winner is ",race(colorss))

time.sleep(5)
