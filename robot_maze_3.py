  #   a115_robot_maze.py
import turtle as trtl

#----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5

#------ robot commands
def move():
  robot.dot(10)
  robot.fd(50)

def turn_left():
  robot.speed(0)
  robot.lt(90)
  robot.speed(2)

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
wn.bgpic("maze3.png") # other file names should be maze2.png, maze3.png

#---- TODO: begin robot movement here
# move robot forward with move()
# turn robot left with turn_left()
# sample while loop:

i = 0
while (i < 2): # forward 3
  move()
  i += 1
  
  i = 0
  while (i < 3):
    turn_left()
    i += 1
  
  i = 0
  while (i < 2):
    move()
    i += 1
  
i = 0
while (i < 1):
  turn_left()
  i += 1
  
  i = 0 
  while (i < 1):
    move()
    i += 1
  robot.pencolor("#32a852")
  i = 0
  while (i < 1):
    move()
    i += 1
  
  i = 0
  while (i < 3):
    turn_left()
    i += 1
  
  i = 0
  while (i < 2):
    move()
    i += 1
  
  i = 0
  while (i < 1):
    turn_left()
    i += 1
  
  i = 0
  while (i < 1):
    move()
    i += 1
  






#---- end robot movement 

wn.mainloop()