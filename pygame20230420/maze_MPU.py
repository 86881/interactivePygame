#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import os
import sys
from pygame.locals import *
import random

try:
    import serial
except ImportError:
    os.system('pip install pyserial')
    import serial

with open('mazeState.txt', 'w') as f:
    f.write('mazeOpening\n')
    f.write('0\n')


if os.path.isfile('com.txt')==False:
    with open('galagaState.txt', 'w') as f:
        f.write('galagaClosed\n')
        f.write('Cant find interactive device!\n')
else:
    with open('com.txt', 'r') as f:
        line=[]
        for i in f:
            i=i.replace('\n','')
            line.append(i)
        try:
            ser = serial.Serial(line[1], int(line[0]),timeout=0.01)
        except :
            with open('galagaState.txt', 'w') as f:
                f.write('galagaClosed\n')
                f.write('Cant find interactive device!\n')
            pygame.quit()
            sys.exit()

    

pygame.init()
pygame.mixer.init()
screen_w,screen_h=1000,750
screen = pygame.display.set_mode((screen_w,screen_h))
pygame.display.set_caption("Maze by 86881")

square=30 #邊緣格子數

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



mcu_feedback_list=[5,0,0,0,0,1,0,0]
mcu_isOnline=False
def mcu():
    global mcu_feedback_list
    global mcu_isOnline
    mcu_feedback = ser.readline().decode()
    
    #print(mcu_feedback)
    
    if(len(mcu_feedback)==21):
        mcu_isOnline=True
        mcu_feedback_list=[]
        if mcu_feedback[0]=='1':#aX
            if mcu_feedback[1]=='0':
                if mcu_feedback[2]=='0':
                    mcu_feedback_list.append(0)#100
                else:
                    mcu_feedback_list.append(+1)#101
            else:
                if mcu_feedback[2]=='0':
                    mcu_feedback_list.append(+2)#110
                else:
                    mcu_feedback_list.append(+3)#111
        else:
            if mcu_feedback[1]=='0':
                if mcu_feedback[2]=='0':
                    mcu_feedback_list.append(0)#000
                else:
                    mcu_feedback_list.append(-1)#001
            else:
                if mcu_feedback[2]=='0':
                    mcu_feedback_list.append(-2)#010
                else:
                    mcu_feedback_list.append(-3)#011

        if mcu_feedback[3]=='1':#aY
            if mcu_feedback[4]=='0':
                if mcu_feedback[5]=='0':
                    mcu_feedback_list.append(0)#100
                else:
                    mcu_feedback_list.append(+1)#101
            else:
                if mcu_feedback[5]=='0':
                    mcu_feedback_list.append(+2)#110
                else:
                    mcu_feedback_list.append(+3)#111
        else:
            if mcu_feedback[4]=='0':
                if mcu_feedback[5]=='0':
                    mcu_feedback_list.append(0)#000
                else:
                    mcu_feedback_list.append(-1)#001
            else:
                if mcu_feedback[5]=='0':
                    mcu_feedback_list.append(-2)#010
                else:
                    mcu_feedback_list.append(-3)#011

        if mcu_feedback[6]=='1':#rX
            if mcu_feedback[7]=='0':
                mcu_feedback_list.append(0)#10   
            else:
                mcu_feedback_list.append(+1)#11
        else:
            if mcu_feedback[7]=='0':
                mcu_feedback_list.append(0)#00
            else:
                mcu_feedback_list.append(-1)#01

        if mcu_feedback[8]=='1':#rY
            if mcu_feedback[9]=='0':
                mcu_feedback_list.append(0)#10   
            else:
                mcu_feedback_list.append(+1)#11
        else:
            if mcu_feedback[9]=='0':
                mcu_feedback_list.append(0)#00
            else:
                mcu_feedback_list.append(-1)#01
        if mcu_feedback[10]=='1':#rZ
            if mcu_feedback[11]=='0':
                mcu_feedback_list.append(0)#10   
            else:
                mcu_feedback_list.append(+1)#11
        else:
            if mcu_feedback[11]=='0':
                mcu_feedback_list.append(0)#00
            else:
                mcu_feedback_list.append(-1)#01
        if mcu_feedback[12]=='1':#sw
            mcu_feedback_list.append(1)#1
        else:
            mcu_feedback_list.append(0)#0

        if mcu_feedback[13]=='1':#vrX
            if mcu_feedback[14]=='0':
                if mcu_feedback[15]=='0':
                    mcu_feedback_list.append(0)#100
                else:
                    mcu_feedback_list.append(+1)#101
            else:
                if mcu_feedback[15]=='0':
                    mcu_feedback_list.append(+2)#110
                else:
                    mcu_feedback_list.append(+3)#111
        else:
            if mcu_feedback[14]=='0':
                if mcu_feedback[15]=='0':
                    mcu_feedback_list.append(0)#000
                else:
                    mcu_feedback_list.append(-1)#001
            else:
                if mcu_feedback[15]=='0':
                    mcu_feedback_list.append(-2)#010
                else:
                    mcu_feedback_list.append(-3)#011

        if mcu_feedback[16]=='1':#vrY
            if mcu_feedback[17]=='0':
                if mcu_feedback[18]=='0':
                    mcu_feedback_list.append(0)#100
                else:
                    mcu_feedback_list.append(+1)#101
            else:
                if mcu_feedback[18]=='0':
                    mcu_feedback_list.append(+2)#110
                else:
                    mcu_feedback_list.append(+3)#111
        else:
            if mcu_feedback[17]=='0':
                if mcu_feedback[18]=='0':
                    mcu_feedback_list.append(0)#000
                else:
                    mcu_feedback_list.append(-1)#001
            else:
                if mcu_feedback[18]=='0':
                    mcu_feedback_list.append(-2)#010
                else:
                    mcu_feedback_list.append(-3)#011
        
        #print(mcu_feedback_list)
    return mcu_feedback_list


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
                #print(mapname,line)
                mazeMapAll[mapCount-1]+=line
        else:
            readMap=False
           
        mapCount+=1



page='home'
running=True
mcu_isOnline=False
def FuncPage(pageF):
    global page
    global running
    if page=='start':
        mapDraw()
        showHeart()
        Player.detect()
        #draw_grid(square)
        edit_img=pygame.image.load('img/edit.png')
        #button.img((0,0),edit_img,(0,255,255),(150,150,150),(150,50),1)
        ball_img=pygame.image.load('img/slime_ball.png')
        screen.blit(ball_img,(x-8,y-8))
        print(mcu())
        
        if mcu_feedback_list[1]>=1:
                    Player.R(mcu_feedback_list[1])
        if mcu_feedback_list[1]<=-1:
                    Player.L(abs(mcu_feedback_list[1]))
        if mcu_feedback_list[0]>=1:
                    Player.U(mcu_feedback_list[0])
        if mcu_feedback_list[0]<=-1:
                    Player.D(abs(mcu_feedback_list[0]))
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

    elif page=="home":
        bg_img=pygame.image.load('img/mazeHome.png')
        screen.blit(bg_img,(0,0))
        start_img=pygame.image.load('img/start_2.png')
        button.img((screen_w/2-100, screen_h*3/4-50),start_img,(0,0,0),(0,0,0),(200,100),1)
        
        pygame.display.update()
        bgm()
        waiting = True
        global mcu_isOnline

        while waiting:
            #print(mcu())
            mcu()
            if mcu_isOnline==False:
                connect_img=pygame.image.load('img/connecting.png')
            else:
                connect_img=pygame.image.load('img/connected.png')

            screen.blit(connect_img, (screen_w/2-50, screen_h*1/2-25))
            pygame.display.update()
            if mcu_feedback_list[6]==-3 :
                    waiting = False
                    screen.blit(bg_img,(0,0))
                    page='start'

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting=False
                    running=False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open('mazeState.txt', 'w') as f:
                    f.write('mazeClosed\n')
                    f.write(str(0))
                running=False
    pygame.display.update()
        
                    
speed=2

class Player:
    def R(change):
        global x
        global y
        global level
        global mazeMap
        global mazeMapAll
        global spawn
        global bumped
        cobblestone=pygame.mixer.Sound("sound/cobblestone.wav")
        glowstone=pygame.mixer.Sound("sound/glowstone.wav")
        
        change=change*(speed**(change-1))


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
        global bumped
        glowstone=pygame.mixer.Sound("sound/glowstone.wav")
        change=change*(speed**(change-1))

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
        global bumped
        glowstone=pygame.mixer.Sound("sound/glowstone.wav")
        change=change*(speed**(change-1))

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
        global bumped
        glowstone=pygame.mixer.Sound("sound/glowstone.wav")
        change=change*(speed**(change-1))

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
    def bump():
        global bumped
        if bumped[0]==False and bumped[1]==False:
            cobblestone=pygame.mixer.Sound("sound/cobblestone.wav")
            cobblestone.play()
            bumped[0],bumped[1]=True,True
            



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
            gold.play()
            x,y = spawn[0],spawn[1]
            heart-=1
 


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
    #pygame.display.update()
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
#print(mazeMap)
#print('mazeMapAll',mazeMapAll)
#print('mazeMap',mazeMap)
level=0
heart=3
bumped=[False,False]
mazeMap=mazeMapAll[level]
while running:
    
    
    screen.fill((0, 0, 0))
    FuncPage(page)
    bgm()
    pygame.display.update()


with open('mazeState.txt', 'w') as f:
    f.write('mazeClosed\n')
    f.write(str(level+1))
pygame.quit()
