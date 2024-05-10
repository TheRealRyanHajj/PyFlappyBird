
import random
import pygame
import sys
#Game Setup
score = 0
y = 100
pygame.init()
gravity = 0
display = pygame.display.set_mode((800, 600))
display.fill((0,0,0))
color = (255,255,255)
GRAY = (115,115,115)
DARKGRAY = (51,51,51)
xValuePipe = 800
xValuePipe2 = 1200
randNum = random.randint(80, 380)
randNum2 = random.randint(80, 380)

BgX=200
Hight=random.randint(75, 300)
BgX2=400
Hight2=random.randint(75, 300)
BgX3=600
Hight3=random.randint(75, 300)
BgX4=800
Hight4=random.randint(75, 300)
BgX5=1000
Hight5=random.randint(75, 300)
BgX6=267
Hight6=random.randint(50, 200)
BgX7=267*2
Hight7=random.randint(50, 200)
BgX8=267*3
Hight8=random.randint(50, 200)

#Deffinition of A Frame for bird
def frame(hi):
    pygame.draw.circle(display, (255,255,255), (100, hi), 30, 5)
#Deffinition Of a Pipe (an obstical)
def framePipe(x,randomNum):
    pygame.draw.rect(display, color, pygame.Rect(x,0,60,randomNum))
    pygame.draw.rect(display, color, pygame.Rect(x,600,60,randomNum-400))

#Deffinition to do collisions on the bird
def collisions(BirdY,PipeX,Num):
    if (not BirdY > Num + 20 or not BirdY < Num + 180) and PipeX < 130 and PipeX > 50:
        return True

#Deffinition Of The Background Code
def frameBackground(color,hight,X,Y,ExtraNum):
    if ExtraNum == 1:
        display.fill((0,0,0))
    pygame.init()
    pygame.draw.rect(display,(color),pygame.Rect(X,Y,196,hight))

#Deffinition Of The Bgs
def frameBgs():
    frameBackground(DARKGRAY,(-1*Hight),int(BgX),600,1)
    frameBackground(DARKGRAY,(-1*Hight2),int(BgX2),600,0)
    frameBackground(DARKGRAY,(-1*Hight3),int(BgX3),600,0)
    frameBackground(DARKGRAY,(-1*Hight4),int(BgX4),600,0)
    frameBackground(DARKGRAY,(-1*Hight5),int(BgX5),600,0)
    frameBackground(GRAY,(-1*Hight6),int(BgX6),600,0)
    frameBackground(GRAY,(-1*Hight7),int(BgX7),600,0)
    frameBackground(GRAY,(-1*Hight8),int(BgX8),600,0)
#Forever Loop
while True:
    #Background Moving
    BgX-=2
    if BgX < -200:
        BgX = 800
        Hight=random.randint(75, 300)
    BgX2-=2
    if BgX2 < -200:
        BgX2 = 800
        Hight2=random.randint(75, 300)
    BgX3-=2
    if BgX3 < -200:
        BgX3 = 800
        Hight3=random.randint(75, 300)
    BgX4-=2
    if BgX4 < -200:
        BgX4 = 800
        Hight4=random.randint(75, 300)
    BgX5-=2
    if BgX5 < -200:
        BgX5 = 800
        Hight5=random.randint(75, 300)
    BgX6-=3
    if BgX6 < -200:
        BgX6 = 800
        Hight6=random.randint(50, 200)
    BgX7-=3
    if BgX7 < -200:
        BgX7 = 800
        Hight7=random.randint(50, 200)
    BgX8-=3
    if BgX8 < -200:
        BgX8 = 800
        Hight8=random.randint(50, 200)
    #Bird Code
    gravity -= 1
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            gravity = 12
    frameBgs() 
    frame(int(y))
    
    #Check And Draw Pipe
    if y > 600:
        break
    elif y < 0:
        y = 0
    else:
        y -= gravity
    if xValuePipe + 60 < 0:
        xValuePipe = 800
        randNum = random.randint(80, 380)
        score += 1
    else:
        xValuePipe -= 4
    if xValuePipe2 + 60 < 0:
        xValuePipe2 = 800
        randNum2 = random.randint(80, 380)
        score += 1
    else:
        xValuePipe2 -= 4
    framePipe(xValuePipe,randNum)
    framePipe(xValuePipe2,randNum2)
    
    if collisions(y,xValuePipe,randNum):
        break
    elif collisions(y,xValuePipe2,randNum2):
        break
#If Game Over then...
print("Game Over, Your Score was:",score)
