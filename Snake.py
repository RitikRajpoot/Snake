import pygame
import random
import sys
pygame.init()
clock=pygame.time.Clock()
screen = pygame.display.set_mode((600,600))
done=False
x=0
y=60
a=300
b=300
w=10
score=0
direction=4
pygame.display.set_caption('Snake')
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 31, 67)
fontObj = pygame.font.Font('freesansbold.ttf', 32)
#direction is right in positive x
while not done:
    screen.fill((255,255,255))
    pressed=pygame.key.get_pressed()
    pygame.draw.rect(screen, BLUE, pygame.Rect(0, 0, 600, 40))
    textSurfaceObj = fontObj.render("                      SNAKE", True, GREEN)
    textRectObj = textSurfaceObj.get_rect()
    screen.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            done= True            
    if pressed[pygame.K_UP]:
        direction=1
    if pressed[pygame.K_DOWN]:
        direction=2
    if pressed[pygame.K_LEFT]:
        direction=3
    if pressed[pygame.K_RIGHT]:
        direction=4
    if direction==1:
        y-=10
    if direction==2:
        y+=10
    if direction==3:
        x-=10
    if direction==4:
        x+=10
    if y<50:
        y=580
    if x<10:
        x=580
    if y>580:
        y=50
    if x>580:
        x=10
    if(x==a) and (y==b):
        a=random.randrange(0,600,10)
        b=random.randrange(40,600,10)
        score+=50
        print(score)
    pygame.draw.rect(screen, (0 ,0 , 255), pygame.Rect(x, y, 10, w))
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(a,b,10,10))
    clock.tick(25)
    pygame.draw.line(screen, (0,0,0),(0,40),(600,40), 20)
    pygame.draw.line(screen, (0,0,0),(0,40),(0,600), 20)
    pygame.draw.line(screen, (0,0,0),(0,600),(600,600), 20)
    pygame.draw.line(screen, (0,0,0),(600,600),(600,40), 20)
    pygame.display.flip()
    
