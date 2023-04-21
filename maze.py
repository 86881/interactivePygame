#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import os
import sys
from pygame.locals import *
import random


with open('mazeState.txt', 'w') as f:
    f.write('mazeOpening\n')
    f.write('0\n')
    

pygame.init()
pygame.mixer.init()
screen_w,screen_h=1000,750
screen = pygame.display.set_mode((screen_w,screen_h))
pygame.display.set_caption("Maze by 86881")

square=30 #��t��l��

x = 500
y = 350

spawn=[500,350]
mazeMapAll=[]
mazeMap=[
         [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
         
         
    
    ]

if os.path.isfile('maze.txt')==False:
    with open('maze.txt', 'w') as f:
        for i in mazeMap:
            tempString=''
            for j in i:
                tempString+=str(j)
                tempString+=","
            f.write(tempString)
            f.write("\n")
else:
    with open('maze.txt', 'r') as f:
        line=[]
        for i in f:
            i=i.replace('\n','')
            i=i.split(",")
            line.append(i[:-1])
        
        line=[[int(j) for j in i ]for i in line]
        #mazeMap=line
        #print(mazeMap)


setting={}
setting_proj=[]
if os.path.isfile('setting.txt')==False:
    with open('mazeState.txt', 'w') as f:
        f.write('mazeClosed\n')
        f.write('Without Setting!\n')
else:
    with open('setting.txt', 'r') as f:
                lineCount=0
                
                for line in f:
                    lineCount+=1
                    line=line.replace("\n","")
                    line=line.replace("{","")
                    line=line.replace("}","")
                    line=line.replace("'","")
                    line=line.replace(",","")
                    
                    if lineCount!=1:
                        line=line.split(':')
                        if len(line)==2:
                            line[0],line[1]=line[0].replace(",",''),line[1].replace(",",'')
                            line[0],line[1]=line[0].replace("\n",''),line[1].replace("\n",'')
                            setting[line[0]]=line[1]
                            setting_proj.append(line[0])
                            print(setting)
                            


def readMap(readMap=True):
    global mazeMapAll
    mazeMapAll=[]
    mapCount=1
    while readMap:
        mapname='maze'+str(mapCount)+'.txt'
        #print(mapname)
        if os.path.isfile(mapname)==True:
            mazeMapAll.append([])
            with open(mapname, 'r') as f:
                line=[]
                for i in f:
                    i=i.replace('\n','')
                    i=i.split(",")
                    line.append(i[:-1])
                line=[[int(j) for j in i ]for i in line]
                print(mapname,line)
                mazeMapAll[mapCount-1]+=line
        else:
            readMap=False
           
        mapCount+=1



page='home'
running=True

def FuncPage(pageF):
    global page
    global running
    
    global setting
    if page=='home':

        mapDraw()
        Player.detect()
        #draw_grid(square)
        edit_img=pygame.image.load('img/edit.png')
        #button.img((0,0),edit_img,(0,255,255),(150,150,150),(150,50),1)
        ball_img=pygame.image.load('img/slime_ball.png')
        screen.blit(ball_img,(x-8,y-8))
        key_pressed = pygame.key.get_pressed()
        
        if key_pressed[pygame.key.key_code(setting['Right'])]:
                    Player.R(1)
        if key_pressed[pygame.key.key_code(setting['Left'])]:
                    Player.L(1)
        if key_pressed[pygame.key.key_code(setting['Forword'])]:
                    Player.U(1)
        if key_pressed[pygame.key.key_code(setting['Backword'])]:
                    Player.D(1)
                   
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                with open('mazeState.txt', 'w') as f:
                    f.write('mazeClosed\n')
                    f.write(str(0))
                running=False
            

                '''
            elif(event.type == pygame.MOUSEBUTTONDOWN):
                mX,mY=pygame.mouse.get_pos()
                #button.img((0,0),edit_img,(0,255,255),(150,150,150),(150,50),1)
                if( (0<mX and mX<150) and (0<mY and mY<50) ):
                    page='edit'
                    '''
    elif page=='edit':
        mapDraw()
        back_img=pygame.image.load('img/back.png')
        save_img=pygame.image.load('img/save.png')
        button.img((0,0),back_img,(0,255,255),(150,150,150),(150,50),1)
        button.img((150,0),save_img,(0,255,255),(150,150,150),(150,50),1)
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                
                running=False
            elif(event.type == pygame.MOUSEBUTTONDOWN):
                mX,mY=pygame.mouse.get_pos()
                #button.img((0,0),edit_img,(0,255,255),(150,150,150),(150,50),1)
                if( (0<mX and mX<150) and (0<mY and mY<50) ):
                    page='home'
                #button.img((0,0),edit_img,(0,255,255),(150,150,150),(150,50),1)
                elif( (150<mX and mX<300) and (0<mY and mY<50) ):
                    
                    with open('maze.txt', 'w') as f:
                        for i in mazeMap:
                            tempString=''
                            for j in i:
                                tempString+=str(j)
                                tempString+=","
                            f.write(tempString)
                            f.write("\n")
                else:
                    if mX/square>mX//square:
                        bX=mX//square
                    else:
                        bX=mX//square-1
                    if mY/square>mY//square:
                        bY=mY//square
                    else:
                        bY=mY//square-1
                    mazeMap[bX][bY]+=1
                    if mazeMap[bX][bY]>4:
                        mazeMap[bX][bY]=0
    pygame.display.update()
        
                    


class Player:
    def R(change):
        global x
        global y
        global level
        global mazeMap
        global mazeMapAll
        global spawn
        glowstone=pygame.mixer.Sound("sound/glowstone.wav")

        mX,mY=x+change,y
        if mX%square>0:
            bX=mX//square
        else:
            bX=mX//square-1
        if mY%square>0:
            bY=mY//square
        else:
            bY=mY//square-1
        #print(mazeMap[bX][bY])
        if x+change<screen_w and mazeMap[bX][bY]!=1:
            x += change
            bumped[0]=False
            if x+change<screen_w and mazeMap[bX][bY]==4:
                level+=1
                mazeMap=mazeMapAll[level]
                spawn[0],spawn[1]=mX,mY
                glowstone.play()
        else:
            Player.bump()
                
 
    def L(change):
        global x
        global y
        global level
        global mazeMap
        global mazeMapAll
        global spawn
        glowstone=pygame.mixer.Sound("sound/glowstone.wav")

        mX,mY=x-change,y

        if mX%square>0:
            bX=mX//square
        else:
            bX=mX//square-1
        if mY%square>0:
            bY=mY//square
        else:
            bY=mY//square-1

        if x-change>0 and mazeMap[bX][bY]!=1:
            x -= change
            bumped[0]=False
            if x-change>0 and mazeMap[bX][bY]==4:
                level+=1
                mazeMap=mazeMapAll[level]
                spawn[0],spawn[1]=mX,mY
                glowstone.play()
        else:
            Player.bump()
 
    def U(change) :
        global x
        global y
        global level
        global mazeMap
        global mazeMapAll
        global spawn
        glowstone=pygame.mixer.Sound("sound/glowstone.wav")

        mX,mY=x,y-change

        if mX%square>0:
            bX=mX//square
        else:
            bX=mX//square-1
        if mY%square>0:
            bY=mY//square
        else:
            bY=mY//square-1

        if y-change>0 and mazeMap[bX][bY]!=1:
            y -= change
            bumped[1]=False
            if y-change>0 and mazeMap[bX][bY]==4:
                level+=1
                mazeMap=mazeMapAll[level]
                spawn[0],spawn[1]=mX,mY
                glowstone.play()
        else:
            Player.bump()
    def D(change):
        global x
        global y
        global level
        global mazeMap
        global mazeMapAll
        global spawn
        glowstone=pygame.mixer.Sound("sound/glowstone.wav")

        mX,mY=x,y+change

        if mX%square>0:
            bX=mX//square
        else:
            bX=mX//square-1
        if mY%square>0:
            bY=mY//square
        else:
            bY=mY//square-1

        if y+change<screen_h and mazeMap[bX][bY]!=1:
            y += change
            bumped[1]=False
            if y+change<screen_h and mazeMap[bX][bY]==4:
                level+=1
                mazeMap=mazeMapAll[level]
                spawn[0],spawn[1]=mX,mY
                glowstone.play()
        else:
            Player.bump()


    def detect():
        
        global x
        global y
        global spawn
        global heart
        mX,mY=x,y
        gold=pygame.mixer.Sound("sound/gold.wav")

        if mX%square>0:
            bX=mX//square
        else:
            bX=mX//square-1
        if mY%square>0:
            bY=mY//square
        else:
            bY=mY//square-1
        if mazeMap[bX][bY]==3:
            x,y = spawn[0],spawn[1]
            gold.play()
            heart-=1
 
            
    def bump():
        global bumped
        if bumped[0]==False and bumped[1]==False:
            cobblestone=pygame.mixer.Sound("sound/cobblestone.wav")
            cobblestone.play()
            bumped[0],bumped[1]=True,True

def draw_grid(pixel):
    for i in range(int(screen_w//pixel)):
        #pygame.draw.line(screen,color,pos1,pos2)
        if(i%10==0):
            pygame.draw.line(screen,(255,0,0),(0,i*pixel),(screen_w,i*pixel))
            pygame.draw.line(screen,(255,0,0),(i*pixel,0),(i*pixel,screen_h))
        elif(i%5==0):
            pygame.draw.line(screen,(0,0,255),(0,i*pixel),(screen_w,i*pixel))
            pygame.draw.line(screen,(0,0,255),(i*pixel,0),(i*pixel,screen_h))
        else:
            pygame.draw.line(screen,(255,255,255),(0,i*pixel),(screen_w,i*pixel))
            pygame.draw.line(screen,(255,255,255),(i*pixel,0),(i*pixel,screen_h))

def word(text,color,pos,size=60):
    head_font = pygame.font.SysFont('Kaisotai-Next-UP-B.ttf', size)
    text_surface = head_font.render(text, True, color)
    screen.blit(text_surface, pos)


def mapDraw():
    img_0=pygame.image.load(os.path.join("img", "coal_block.png")).convert()
    img_0=pygame.transform.scale(img_0,(square,square))
    img_1=pygame.image.load(os.path.join("img", "cobblestone.png")).convert()
    img_1=pygame.transform.scale(img_1,(square,square))
    img_2=pygame.image.load(os.path.join("img", "smooth_stone.png")).convert()
    img_2=pygame.transform.scale(img_2,(square,square))
    img_3=pygame.image.load(os.path.join("img", "gold_block.png")).convert()
    img_3=pygame.transform.scale(img_3,(square,square))
    img_4=pygame.image.load(os.path.join("img", "glowstone.png")).convert()
    img_4=pygame.transform.scale(img_4,(square,square))
    for i in range(0,screen_w,square):
        for j in range(0,screen_h,square):
            x=i//square
            y=j//square

            #print(x,y,screen_w//square,screen_h//square)
            if x>=screen_w//square or y>=screen_h//square:
                break

            if mazeMap[x][y]==0:
                screen.blit(img_0,(i,j)) 
            elif mazeMap[x][y]==1:
                screen.blit(img_1,(i,j)) 
            elif mazeMap[x][y]==2:
                screen.blit(img_2,(i,j)) 
            elif mazeMap[x][y]==3:
                screen.blit(img_3,(i,j)) 
            elif mazeMap[x][y]==4:
                screen.blit(img_4,(i,j)) 


class button():

    def img(pos,text,color,bgcolor,size,line):
        x,y=pos
        dx,dy=size
        mX,mY=pygame.mouse.get_pos()

        if((x<mX and mX<dx+x) and (y<mY and mY<dy+y)):
            pygame.draw.rect(screen,(255,255,255),[x-line,y-line,dx+line*2,dy+line*2])
            pygame.draw.rect(screen,bgcolor,[x,y,dx,dy])
        else:
            pygame.draw.rect(screen,(0,0,0),[x-line,y-line,dx+line*2,dy+line*2])
            pygame.draw.rect(screen,bgcolor,[x,y,dx,dy])
        #word(text,color,pos)
        screen.blit(text,pos) 
    def text(pos,text,color,bgcolor,size,line,Fsize=60):
        x,y=pos
        dx,dy=size
        mX,mY=pygame.mouse.get_pos()

        if((x<mX and mX<dx+x) and (y<mY and mY<dy+y)):
            pygame.draw.rect(screen,(255,255,255),[x-line,y-line,dx+line*2,dy+line*2])
            pygame.draw.rect(screen,bgcolor,[x,y,dx,dy])
        else:
            pygame.draw.rect(screen,(0,0,0),[x-line,y-line,dx+line*2,dy+line*2])
            pygame.draw.rect(screen,bgcolor,[x,y,dx,dy])
        word(text,color,pos,Fsize)
        
def showHeart():
    global heart
    global running
    pos=[800,10]
    ball_img=pygame.image.load('img/slime_ball.png')
    for i in range(heart):
        screen.blit(ball_img,(pos[0]+i*20,pos[1]))
    pygame.display.update()
    if heart<=0:
        running=False

            
def bgm():
    if pygame.mixer.music.get_busy()==False:
        pygame.mixer.music.load("sound/bg.ogg")
        pygame.mixer.music.play()
        pygame.mixer.music.set_pos(random.randint(0,int(pygame.mixer.Sound("sound/bg.ogg").get_length())))
        print(pygame.mixer.music.get_pos())
        #print(pygame.mixer.Sound("sound/bg.ogg").get_length())

readMap()
print(mazeMap)
print('mazeMapAll',mazeMapAll)
print('mazeMap',mazeMap)
level=0
heart=3
bumped=[False,False]
mazeMap=mazeMapAll[level]
while running:
    screen.fill((0, 0, 0))
    FuncPage(page)
    showHeart()
    bgm()

    pygame.display.update()


with open('mazeState.txt', 'w') as f:
    f.write('mazeClosed\n')
    f.write(str(level+1))
pygame.quit()
