  #   a115_robot_maze.py
import turtle as trtl

#----- maze and turtle config variables
screen_h = 690
screen_w = 720
startx = -335
starty = -325
turtle_scale = 0.5

#------ robot commands
def move():
    robot.dot(10)
    robot.fd(28)
    robot.speed(0)

def turn_left():
    robot.speed(0)
    robot.lt(90)
    robot.speed(0)

#----- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "robot.gif"
wn.addshape(robot_image)

#----- init robot
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.color("darkorchid")
robot.pencolor("darkorchid")
robot.penup()
robot.setheading(90)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()

#---- TODO: change maze here
wn.bgpic("robot_maze_challenge.png") # other file names should be maze2.png, maze3.png

#---- TODO: begin robot movement here
# move robot forward with move()
# turn robot left with turn_left()
# sample while loop:

i = 0
while (i < 3): # turns right
  turn_left()
  i += 1 

i = 0
while (i < 24): # forward 3
    move()
    i += 1 

i = 0
while (i < 1):
    turn_left()
    i += 1 
    while(i < 24):
        move()
        i += 1

i = 0
while (i < 1):
    turn_left()
    i += 1 
    while(i < 25):
        move()
        i += 1
i = 0
while (i < 1):
    turn_left()
    i += 1 
    while(i < 20):
        move()
        i += 1
i = 0
while (i < 1):
    turn_left()
    i += 1 
    while(i < 21):
        move()
        i += 1
i = 0
while (i < 1):
    turn_left()
    i += 1 
    while(i < 16):
        move()
        i += 1
i = 0
while (i < 1):
    turn_left()
    i += 1 
    while(i < 17):
        move()
        i += 1
i = 0
while (i < 1):
    turn_left()
    i += 1 
    while(i < 12):
        move()
        i += 1
i = 0
while (i < 1):
    turn_left()
    i += 1 
    while(i < 13):
        move()
        i += 1
i = 0
while (i < 1):
    turn_left()
    i += 1 
    while(i < 8):
        move()
        i += 1
i = 0
while (i < 1):
    turn_left()
    i += 1 
    while(i < 9):
        move()
        i += 1
i = 0
while (i < 1):
    turn_left()
    i += 1 
    while(i < 4):
        move()
        i += 1
i = 0
while (i < 1):
    turn_left()
    i += 1 
    while(i < 4):
        move()
        i += 1
i = 0
while (i < 1):
    turn_left()
    i += 1 
    while(i < 2):
        move()
        i += 1
i = 0
while (i < 3):
    turn_left()
    i += 1 
i = 0
while(i < 3):
    move()
    i += 1
i = 0
while (i < 3):
    turn_left()
    i += 1 
i = 0
while(i < 3):
    move()
    i += 1
i = 0
while (i < 3):
    turn_left()
    i += 1
i = 0
while(i < 8):
    move()
    i += 1
i = 0
while (i < 3):
    turn_left()
    i += 1
i = 0
while(i < 7):
    move()
    i += 1
i = 0
while (i < 3):
    turn_left()
    i += 1
i = 0
while(i < 12):
    move()
    i += 1
i = 0
while (i < 3):
    turn_left()
    i += 1
i = 0
while(i < 11):
    move()
    i += 1
i = 0
while (i < 3):
    turn_left()
    i += 1
i = 0
while(i < 16):
    move()
    i += 1
i = 0
while (i < 3):
    turn_left()
    i += 1
i = 0
while(i < 15):
    move()
    i += 1
i = 0
while (i < 3):
    turn_left()
    i += 1
i = 0
while(i < 20):
    move()
    i += 1
i = 0
while (i < 3):
    turn_left()
    i += 1
i = 0
while(i < 19):
    move()
    i += 1
i = 0
while (i < 3):
    turn_left()
    i += 1
i = 0
while(i < 22):
    move()
    i += 1
#---- end robot movement 

wn.mainloop()