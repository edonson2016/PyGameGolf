import math
import random
import pygame
from golfClass import *
import os
import platform
import sys

direct = __file__[0:-12]

if platform.system() == 'Windows':
    direct.replace("\\", "\\\"")
    I3_1 = direct + "\\field3-1.png"
    I2_1 = direct + "\\field2-1.png"
    I1_1 = direct + "\\field1-1.png"
else:
    I3_1 = direct + "/field3-1.png"
    I2_1 = direct + "/field2-1.png"
    I1_1 = direct + "/field1-1.png"
# Initialize pygame
pygame.init()

#Creates vector field object from class VField using a locally stored image
#fieldImage = "C:\\Users\\edons\\Onedrive\\Desktop\\VSC Files\\pyGameGolf\\reField.png"
f3_1 = lambda x, y: (y, -math.sin(x))
#v3_1 = Vfield("C:\\Users\\edons\\Onedrive\\Desktop\\VSC Files\\pyGameGolf\\field3-1.png", f3_1, (-10, 10), (-5, 5), 650, 650)
v3_1 = Vfield(I3_1, f3_1, (-10, 10), (-5, 5), 650, 650)

f2_1 = lambda x, y: (math.sin(x+y), math.cos(x-y))
#v2_1 = Vfield("C:\\Users\\edons\\Onedrive\\Desktop\\VSC Files\\pyGameGolf\\field2-1.png", f2_1, (-2, 2), (-2, 2), 650, 650)
v2_1 = Vfield(I2_1, f2_1, (-2, 2), (-2, 2), 650, 650)

f1_1 = lambda x, y: (x-x**3, -y)
#v1_1 = Vfield("C:\\Users\\edons\\Onedrive\\Desktop\\VSC Files\\pyGameGolf\\field1-1.png", f1_1, (-2, 2), (-2, 2), 650, 650)
v1_1 = Vfield(I1_1, f1_1, (-2, 2), (-2, 2), 650, 650)

levels = [v1_1, v2_1, v3_1]
vField = None
#Creates a ball from class Ball and Goal from class Goal
#ball = Ball(screen = vField.screen, coords = (250, 250), radius = 10, color = (255, 0, 0))
#goal = Goal(screen = vField.screen, coords = (random.randint(0,vField.xPix), random.randint(0,vField.yPix)), radius = 10, color = (0,0,0))

#Creates pygame screen
#screen = vField.screen

#Sets a caption for the window
pygame.display.set_caption("Vector Field Golf")

#Sets while loop conditions
#done = False
clock = pygame.time.Clock()
#selects goal positions for each level
goal0 = (random.randint(650//3,2*650//3),random.randint(650//3,2*650//3))
goal1 = ((random.randint(10,100),random.randint(300,450)),(random.randint(350,640),random.randint(50,300)))[random.randint(0,1)]
goal2 = ((random.randint(10,200), random.randint(450,600)), (random.randint(450,640), random.randint(450,600)), (random.randint(80,570), (-1)**random.randint(1,2)*random.randint(50,300) + 650//2))[random.randint(0,2)]
goalset = [goal0, goal1, goal2]
#Temp statemnet: mouse shit

mouseClicked = False
speed = 1
level = 0
Total = 0
while(level < 3):
    if levels[level] != vField:
        vField = levels[level]
        ball = Ball(screen = vField.screen, coords = (250, 250), radius = 10, color = (255, 0, 0))
        goal = Goal(screen = vField.screen, coords = goalset[level], radius = 10, color = (0,0,0))
    #This limits the while loop to 60 times per second
    clock.tick(60)

    #If user clicks the exit out then the loop will end
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #Tests if user clicks and sets a variable equal to pos at that click
    if (True in pygame.mouse.get_pressed()):
        mouseClicked = True
        mousePos = pygame.mouse.get_pos()

    #Temp statement: Will remove once we get actual pictures of vector fields
    vField.screen.fill("white")

    #Updates the screen
    vField.updateScreen()

    #Ball updating
    ball.active = mouseClicked
    acc = vField.calc(ball.coords)
    ball.update((speed * acc[0], speed * acc[1]))

    #Goal Updating
    goal.draw()
    if (mouseClicked):
        if goal.madeGoal(ball.coords, ball.radius):
            print(ball.score)
            Total += ball.score
            ball.score = 0
            level += 1
            mouseClicked = False
            #done = True

    #If the ball exits the boundary then the game will quit
    if (ball.coords[0] > vField.xPix or ball.coords[0] < 0):
        #done = True
        ball.active = False
        mouseClicked = False
        ball.score = 0
    
    if (ball.coords[1] > vField.yPix or ball.coords[1] < 0):
        #done = True
        ball.active = False
        mouseClicked = False
        ball.score = 0

    #Updates everything
    pygame.display.update()
print(f'Your Total Score was {round(Total)}')
pygame.quit()





     