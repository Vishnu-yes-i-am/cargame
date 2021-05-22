import pygame
from pygame import mixer
from playsound import playsound
import random
import time
clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("Car_Racing By VISHNU")
display=pygame.display.set_mode((1200,720))
#defining colors
white=pygame.Color(255, 255, 255)
black=pygame.Color(0, 0, 0)
green=pygame.Color(98, 244, 68)
blue=pygame.Color(111, 148, 191)
red=pygame.Color(250, 0, 0)
#------------------
cars=[r"car1.jpg",r"car2.jpg",r"car3.jpg",r"car4.jpg",r"car5.jpg",r"car6.jpg",r"car7.jpg",r"car8.jpg",r"car9.jpg"]
font=pygame.font.SysFont("Algerian", 50)
newgame=True
f=open("highscore.txt",'r')
k=f.readlines()
highscore=int(k[0])
mixer.init()
mixer.music.load("theme.wav")
car=pygame.transform.rotate(pygame.image.load(random.choice(cars)),90)
while newgame:
    display.fill(blue)
    display.blit(font.render("Starting The Game....", True, red), (200,400))
    pygame.display.update()
    pygame.time.wait(2*1000)
    mixer.music.play()
    y=0
    y1=200
    y2=400
    y3=600
    xx=220
    yy=500
    bx=bx=random.choice([200,400,600])
    r=1
    by=-270
    score=0
    speed=7
    rect1=pygame.Rect(812, 0, 400, 780)
    rect2=pygame.Rect(0, 0, 190, 780)
    gameover=False
    while not gameover:
        clock.tick(60)
        y+=speed
        y1+=speed
        y2+=speed
        y3+=speed
        by+=speed-3
        if score>5*r:
            playsound("horn.wav",False)
            speed+=2
            r+=1
        if y>700:
            y=-100
        if y<-100:
            y=700
        if y1>700:
            y1=-100
        if y1<-100:
            y1=700
        if y2<-100:
            y2=700
        if y3<-100:
            y3=700
        if y2>700:
            y2=-100
        if y3>700:
            y3=-100
        display.fill(white)
        if by>700:
            by=-270
            score+=1
            bx=random.choice([200,400,600])
            car=pygame.transform.rotate(pygame.image.load(random.choice(cars)),90)
        pic2=pygame.transform.scale(car, (180,270))
        display.blit(pic2,(bx,by))
        pygame.draw.line(display, black, (200,y), (200,y+130),16)
        pygame.draw.line(display, black, (200,y1), (200,y1+130),16)
        pygame.draw.line(display, black, (200,y2), (200,y2+130),16)
        pygame.draw.line(display, black, (200,y3), (200,y3+130),16)
        pygame.draw.line(display, black, (400,y), (400,y+130),16)
        pygame.draw.line(display, black, (400,y1), (400,y1+130),16)
        pygame.draw.line(display, black, (400,y2), (400,y2+130),16)
        pygame.draw.line(display, black, (400,y3), (400,y3+130),16)
        pygame.draw.line(display, black, (600,y), (600,y+130),16)
        pygame.draw.line(display, black, (600,y1), (600,y1+130),16)
        pygame.draw.line(display, black, (600,y2), (600,y2+130),16)
        pygame.draw.line(display, black, (600,y3), (600,y3+130),16)
        pygame.draw.line(display, black, (800,y), (800,y+130),16)
        pygame.draw.line(display, black, (800,y1), (800,y1+130),16)
        pygame.draw.line(display, black, (800,y2), (800,y2+130),16)
        pygame.draw.line(display, black, (800,y3), (800,y3+130),16)
        pic=pygame.image.load("car.jpg")
        pic=pygame.transform.rotate(pic, 270)
        pic=pygame.transform.scale(pic, (160,200))
        display.blit(pic, (xx,yy))
        pygame.draw.rect(display, green, rect1)
        pygame.draw.rect(display, green, rect2)
        display.blit(font.render("Score: "+str(score),True, black),(850,100))
        display.blit(font.render("High Score: "+str(highscore),True, black),(830,230))
        pygame.display.update()
        if pygame.Rect(bx,by,180,270).colliderect((xx,yy,160,200)):
            speed=0
            mixer.music.stop()
            playsound("boom.wav")
            gameover=True
            display.blit(font.render("Game Over",True, red),(300,400))
            pygame.display.update()
            pygame.time.wait(3000)
            display.fill(blue)
            display.blit(font.render("your score is :"+str(score),True, red),(200,400))
            if score>highscore:
                f2=open("highscore.txt",'w')
                f2.write(str(score))
                display.blit(font.render("Great you had beaten the high score",True, green),(150,200))
            highscore=max(score,highscore)
            display.blit(font.render("press 'y' to play again else 'n' to quit.",True, green),(50,600))
            pygame.display.update()
            responsed=False
            while not responsed:
                for el in pygame.event.get():
                    if el.type==pygame.KEYDOWN:
                        if el.key==pygame.K_n:
                            pygame.quit()
                            quit()
                        if el.key==pygame.K_y:
                            newgame=True
                            responsed=True
                            break
                    elif el.type==pygame.QUIT:
                        pygame.quit()
                        quit()
        for el in pygame.event.get():
            if el.type==pygame.KEYDOWN:
                if el.key==pygame.K_UP and yy>100:
                    yy-=50
                    break
                if el.key==pygame.K_DOWN and yy<500:
                    yy+=50
                    break
                if el.key==pygame.K_RIGHT and xx<600:
                    xx+=200
                    break
                if el.key==pygame.K_LEFT and xx>300:
                    xx-=200
                    break
                if el.key==pygame.K_SPACE:
                    playsound('classic.wav',False) 
            elif el.type==pygame.QUIT:
                pygame.quit()
                quit()
    
