#!/usr/bin/python
# -*- coding: utf-8 -*-
# 20230317註解版本
# from asyncio.windows_events import NULL

import os
from lib2to3 import pygram
import sys
from tkinter import FALSE
try:
    import pygame
except ImportError:
    os.system('pip install pygame')
    import pygame
from pygame.locals import *
import time

# 互動裝置連線設定
if os.path.isfile('com.txt') == False:
    with open('com.txt', 'w') as f:
        f.write('115200\n')
        f.write('COM7\n')

InteractiveDevice = False


# 遊戲初始化
pygame.init()
pygame.mixer.init()
screen_w, screen_h = 1000, 600
screen = pygame.display.set_mode((screen_w, screen_h))
global page
page = 'home'
scoreWrited = False
clock = pygame.time.Clock()


# 頁面
def FuncPage(pageF):
    global page
    global scoreWrited
    global InteractiveDevice
    if (pageF == "home"):  # 首頁
        # img
        bg_img = pygame.image.load('img/bg.png')
        quit_img = pygame.image.load('img/quit.png')
        setting_img = pygame.image.load('img/setting.png')
        start_img = pygame.image.load('img/start.png')
        screen.blit(bg_img, (0, 0))
        # draw_grid(100)
        word('v0.2', (255, 255, 255), (0, 575), 40)
        word('©2023', (255, 255, 255), (900, 575), 40)
        button.img((550, 400), quit_img, (0, 255, 255),
                   (150, 150, 150), (150, 50), 1)
        button.img((300, 400), setting_img, (0, 255, 255),
                   (150, 150, 150), (150, 50), 1)
        button.img((300, 300), start_img, (0, 255, 255),
                   (150, 150, 150), (400, 50), 1)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                mX, mY = pygame.mouse.get_pos()
                # button.create((550,400),"Quit",(0,255,255),(150,150,150),(150,50),1)
                if ((550 < mX and mX < 700) and (400 < mY and mY < 450)):
                    pygame.quit()
                    sys.exit()
                # button.create((300,400),"Setting",(0,255,255),(150,150,150),(150,50),1)
                elif ((300 < mX and mX < 450) and (400 < mY and mY < 450)):
                    print("setting")

                    page = 'setting'
                # button.create((300,300),"Start",(0,255,255),(150,150,150),(400,50),1)
                elif ((300 < mX and mX < 700) and (300 < mY and mY < 350)):
                    page = 'game'
                    print("game")
                # word('©2023',(255,255,255),(900,575),40)
                elif ((900 < mX and mX < 1000) and (575 < mY and mY < 600)):
                    print("copyright")
                    page = "copyright"

    elif (pageF == 'copyright'):  # 版權宣告頁
        # img
        bg_img = pygame.image.load('img/bg_copyright.png')
        back_img = pygame.image.load('img/back.png')
        list_img = pygame.image.load('img/copyrightList.png')
        screen.blit(bg_img, (0, 0))
        screen.blit(list_img, (200, 50))
        # draw_grid(100)
        button.img((0, 0), back_img, (0, 255, 255),
                   (150, 150, 150), (150, 50), 1)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                mX, mY = pygame.mouse.get_pos()
                # button.img((0,0),back_img,(0,255,255),(150,150,150),(150,50),1)
                if ((0 < mX and mX < 150) and (0 < mY and mY < 50)):

                    print("home")
                    page = 'home'

    elif (pageF == 'game'):  # 遊戲選單
        # img
        bg_img = pygame.image.load('img/bg_game.png')
        back_img = pygame.image.load('img/back.png')
        galaga_img = pygame.image.load('img/btn_galaga.png')
        ball_img = pygame.image.load('img/ball.png')
        screen.blit(bg_img, (0, 0))
        galaga_score = [0]
        if os.path.isfile('score.txt') == True:
            with open('score.txt', 'r') as f:
                for line in f:
                    line = line.split()
                    galaga_score.append(line[0])
            galaga_score.sort
        maze_score = [0]
        if os.path.isfile('mazescore.txt') == True:
            with open('mazescore.txt', 'r') as f:
                for line in f:
                    line = line.split()
                    maze_score.append(line[0])
            maze_score.sort
        # draw_grid(100)
        button.img((0, 0), back_img, (0, 255, 255),
                   (150, 150, 150), (150, 50), 1)
        button.img((100, 100), galaga_img, (0, 255, 255),
                   (150, 150, 150), (200, 250), 1)
        button.img((400, 100), ball_img, (0, 255, 255),
                   (150, 150, 150), (200, 250), 1)

        word('Highest:', (0, 0, 0), (100, 380), 40)
        word(str(galaga_score[-1]), (0, 0, 0), (250, 380), 40)
        word('Highest:', (0, 0, 0), (400, 380), 40)
        word(str(maze_score[-1]), (0, 0, 0), (550, 380), 40)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                mX, mY = pygame.mouse.get_pos()
                # button.img((0,0),back_img,(0,255,255),(150,150,150),(150,50),1)
                if ((0 < mX and mX < 150) and (0 < mY and mY < 50)):

                    print("home")
                    page = 'home'
                # button.img((100,100),galaga_img,(0,255,255),(150,150,150),(200,250),1)
                elif ((100 < mX and mX < 300) and (100 < mY and mY < 350)):
                    print("galaga")
                    if InteractiveDevice == False:
                        os.system('python galaga.py')
                    else:
                        os.system('python galaga_MPU.py')
                    print("galaga")
                    page = 'galaga'
                    scoreWrited = False
                # button.img((400,100),ball_img,(0,255,255),(150,150,150),(200,250),1)
                elif ((400 < mX and mX < 600) and (100 < mY and mY < 350)):
                    if InteractiveDevice == False:
                        os.system('python maze.py')
                    else:
                        os.system('python maze_MPU.py')
                    print("maze")
                    page = 'maze'
                    scoreWrited = False

    elif (pageF == 'setting'):  # 設定頁
        global COM_PORT

        setlist = []
        # img
        bg_img = pygame.image.load('img/bg_setting.png')
        back_img = pygame.image.load('img/back.png')
        reset_img = pygame.image.load('img/setting_reset.png')
        modify_img = pygame.image.load('img/setting_modify.png')

        screen.blit(bg_img, (0, 0))
        # draw_grid(100)
        button.img((0, 0), back_img, (0, 255, 255),
                   (150, 150, 150), (150, 50), 1)
        button.img((100, 500), reset_img, (0, 255, 255),
                   (150, 150, 150), (150, 50), 1)
        word('Interactive Device', (255, 255, 255), (700, 100), 30)
        button.text((700, 150), 'On', (0, 0, 0),
                    (150, 150, 150), (80, 30), 1, 30)
        # button.text((700,200),'COM4',(0,0,0),(150,150,150),(80,30),1,30)
        # button.text((700,250),'COM5',(0,0,0),(150,150,150),(80,30),1,30)
        button.text((700, 200), 'Off', (0, 0, 0),
                    (150, 150, 150), (80, 30), 1, 30)
        if os.path.isfile('setting.txt') == False:
            with open('setting.txt', 'w') as f:
                f.write('Setting Created at ')
                f.write(time.ctime(time.time()))
                f.write('\n')
                f.write('{\n')
                defaultSetting = ["'Forword':'W',\n", "'Backword':'S',\n", "'Left':'A',\n",
                                  "'Right':'D'\n", "'Shoot':'Space'\n", "'Pause':'escape'\n", '}\n']
                f.writelines(defaultSetting)
        with open('setting.txt', 'r') as f:
            printY = 100

            for line in f:
                line = line.replace("\n", "")
                line = line.replace("{", "")
                line = line.replace("}", "")
                line = line.replace("'", "")
                line = line.replace(",", "")

                if printY == 100:
                    word(line, (255, 255, 255), (100, printY), 30)
                    printY += 30
                else:
                    line = line.split(':')
                    if len(line) == 2:
                        word(line[0], (255, 255, 255), (100, printY), 30)
                        word(':', (255, 255, 255), (200, printY), 30)
                        word(line[1], (0, 0, 0), (220, printY), 30)
                        line[0], line[1] = line[0].replace(
                            ",", ''), line[1].replace(",", '')
                        line[0], line[1] = line[0].replace(
                            "\n", ''), line[1].replace("\n", '')
                        tempString = [line[0], line[1]]
                        setlist.append(tempString)
                        button.img((300, printY), modify_img,
                                   (0, 255, 255), (150, 150, 150), (50, 30), 1)
                        printY += 30

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                mX, mY = pygame.mouse.get_pos()
                # button.img((0,0),back_img,(0,255,255),(150,150,150),(150,50),1)
                if ((0 < mX and mX < 150) and (0 < mY and mY < 50)):

                    print("home")
                    page = 'home'
                # button.img((100,500),reset_img,(0,255,255),(150,150,150),(150,50),1)
                elif ((100 < mX and mX < 250) and (500 < mY and mY < 550)):
                    print("reset")
                    with open('setting.txt', 'w') as f:
                        f.write('Setting Created at ')
                        f.write(time.ctime(time.time()))
                        f.write('\n')
                        defaultSetting = ["'Forword':'W',\n", "'Backword':'S',\n", "'Left':'A',\n",
                                          "'Right':'D'\n", "'Shoot':'Space'\n", "'Pause':'escape'\n", '}\n']
                        f.writelines(defaultSetting)
                # button.img((300,printY),modify_img,(0,255,255),(150,150,150),(50,30),1)
                elif ((300 < mX and mX < 350) and (130 < mY and mY < (130+30*len(setlist)))):
                    print(setlist)
                    if (mY-130) % 30 != 0:
                        num = (mY-130)//30+1
                    else:
                        num = (mY-130)//30

                    pygame.event.clear()
                    keyValue = [pygame.K_BACKSPACE, pygame.K_TAB, pygame.K_CLEAR, pygame.K_RETURN, pygame.K_PAUSE, pygame.K_ESCAPE, pygame.K_SPACE, pygame.K_EXCLAIM, pygame.K_QUOTEDBL, pygame.K_HASH, pygame.K_DOLLAR, pygame.K_AMPERSAND, pygame.K_QUOTE, pygame.K_LEFTPAREN, pygame.K_RIGHTPAREN, pygame.K_ASTERISK, pygame.K_PLUS, pygame.K_COMMA, pygame.K_MINUS, pygame.K_PERIOD, pygame.K_SLASH, pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9, pygame.K_COLON, pygame.K_SEMICOLON, pygame.K_LESS, pygame.K_EQUALS, pygame.K_GREATER, pygame.K_QUESTION, pygame.K_AT, pygame.K_LEFTBRACKET, pygame.K_BACKSLASH, pygame.K_RIGHTBRACKET, pygame.K_CARET, pygame.K_UNDERSCORE, pygame.K_BACKQUOTE, pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_m, pygame.K_n, pygame.K_o, pygame.K_p, pygame.K_q, pygame.K_r, pygame.K_s, pygame.K_t, pygame.K_u, pygame.K_v, pygame.K_w, pygame.K_x,
                                pygame.K_y, pygame.K_z, pygame.K_DELETE, pygame.K_KP0, pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4, pygame.K_KP5, pygame.K_KP6, pygame.K_KP7, pygame.K_KP8, pygame.K_KP9, pygame.K_KP_PERIOD, pygame.K_KP_DIVIDE, pygame.K_KP_MULTIPLY, pygame.K_KP_MINUS, pygame.K_KP_PLUS, pygame.K_KP_ENTER, pygame.K_KP_EQUALS, pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT, pygame.K_INSERT, pygame.K_HOME, pygame.K_END, pygame.K_PAGEUP, pygame.K_PAGEDOWN, pygame.K_F1, pygame.K_F2, pygame.K_F3, pygame.K_F4, pygame.K_F5, pygame.K_F6, pygame.K_F7, pygame.K_F8, pygame.K_F9, pygame.K_F10, pygame.K_F11, pygame.K_F12, pygame.K_F13, pygame.K_F14, pygame.K_F15, pygame.K_NUMLOCK, pygame.K_CAPSLOCK, pygame.K_SCROLLOCK, pygame.K_RSHIFT, pygame.K_LSHIFT, pygame.K_RCTRL, pygame.K_LCTRL, pygame.K_RALT, pygame.K_LALT, pygame.K_RMETA, pygame.K_LMETA, pygame.K_LSUPER, pygame.K_RSUPER, pygame.K_MODE, pygame.K_HELP, pygame.K_PRINT, pygame.K_SYSREQ, pygame.K_BREAK, pygame.K_MENU, pygame.K_POWER, pygame.K_EURO, pygame.K_AC_BACK]
                    for i in keyValue:
                        if (pygame.key.get_pressed()[i] == True):
                            print(pygame.key.name(i))
                            setlist[num-1][1] = pygame.key.name(i)
                            break

                    # setlist[num-1][1]='X'
                    tempString = []
                    for line in setlist:
                        # print(line)
                        tempString.append("'"+line[0]+"':'"+line[1]+"',\n")
                    with open('setting.txt', 'w') as f:
                        f.write('Setting Modify at ')
                        f.write(time.ctime(time.time()))
                        f.write('\n')
                        f.write('{\n')
                        # print(tempString)
                        f.writelines(tempString)
                        f.write('}\n')
                    print('modify')
                # button.text((700,150),'On',(0,255,255),(150,150,150),(80,30),1,30)

                elif (700 < mX and mX < 780 and 150 < mY and mY < 380):
                    if ((700 < mX and mX < 780) and (150 < mY and mY < 180)):
                        InteractiveDevice = True
                        print('On')

                    # button.text((700,200),'COM4',(0,0,0),(150,150,150),(80,30),1,30)
                    elif ((700 < mX and mX < 780) and (200 < mY and mY < 230)):
                        InteractiveDevice = False

                        print('off')
    elif (pageF == 'galaga'):  # galaga
        # img
        bg_img = pygame.image.load('img/bg_galaga.png')
        back_img = pygame.image.load('img/back.png')
        screen.blit(bg_img, (0, 0))
        # draw_grid(100)
        button.img((0, 0), back_img, (0, 255, 255),
                   (150, 150, 150), (150, 50), 1)
        if os.path.isfile('galagaState.txt') == True:
            with open('galagaState.txt', 'r') as f:
                printY = 100
                for line in f:
                    line.replace('\n', '')
                    word(line, (255, 255, 255), (100, printY), 30)
                    if (printY == 130 and scoreWrited == False):
                        with open('score.txt', 'a') as f2:
                            f2.write(line)
                            f2.write(' ')
                            f2.write(time.ctime(time.time()))
                            f2.write('\n')
                            scoreWrited = True

                    printY += 30

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                mX, mY = pygame.mouse.get_pos()
                # button.img((0,0),back_img,(0,255,255),(150,150,150),(150,50),1)
                if ((0 < mX and mX < 150) and (0 < mY and mY < 50)):

                    print("home")
                    page = 'home'
    elif (pageF == 'maze'):  # maze
        # img
        bg_img = pygame.image.load('img/bg_game.png')
        back_img = pygame.image.load('img/back.png')
        screen.blit(bg_img, (0, 0))
        # draw_grid(100)
        button.img((0, 0), back_img, (0, 255, 255),
                   (150, 150, 150), (150, 50), 1)
        if os.path.isfile('mazeState.txt') == True:
            with open('mazeState.txt', 'r') as f:
                printY = 100
                for line in f:
                    line.replace('\n', '')
                    word(line, (255, 255, 255), (100, printY), 30)
                    if (printY == 130 and scoreWrited == False):
                        with open('mazescore.txt', 'a') as f2:
                            f2.write(line)
                            f2.write(' ')
                            f2.write(time.ctime(time.time()))
                            f2.write('\n')
                            scoreWrited = True

                    printY += 30

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                mX, mY = pygame.mouse.get_pos()
                # button.img((0,0),back_img,(0,255,255),(150,150,150),(150,50),1)
                if ((0 < mX and mX < 150) and (0 < mY and mY < 50)):

                    print("home")
                    page = 'home'

    pygame.display.update()


'''範本
    elif(pageF==''):
        #img
        bg_img = pygame.image.load('img/bg_copyright.png')
        back_img = pygame.image.load('img/back.png')
        screen.blit(bg_img,(0,0)) 
        draw_grid(100)
        button.img((0,0),back_img,(0,255,255),(150,150,150),(150,50),1)
        

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif(event.type == pygame.MOUSEBUTTONDOWN):
                mX,mY=pygame.mouse.get_pos()
                #button.img((0,0),back_img,(0,255,255),(150,150,150),(150,50),1)
                if( (0<mX and mX<150) and (0<mY and mY<50) ):   
                    
                    print("home")
                    page='home'
                

'''


def draw_grid(pixel):  # 畫定位框
    for i in range(int(screen_w//pixel)):
        # pygame.draw.line(screen,color,pos1,pos2)
        if (i % 10 == 0):
            pygame.draw.line(screen, (255, 0, 0),
                             (0, i*pixel), (screen_w, i*pixel))
            pygame.draw.line(screen, (255, 0, 0),
                             (i*pixel, 0), (i*pixel, screen_h))
        elif (i % 5 == 0):
            pygame.draw.line(screen, (0, 0, 255),
                             (0, i*pixel), (screen_w, i*pixel))
            pygame.draw.line(screen, (0, 0, 255),
                             (i*pixel, 0), (i*pixel, screen_h))
        else:
            pygame.draw.line(screen, (255, 255, 255),
                             (0, i*pixel), (screen_w, i*pixel))
            pygame.draw.line(screen, (255, 255, 255),
                             (i*pixel, 0), (i*pixel, screen_h))


def word(text, color, pos, size=60):  # 顯示文字
    head_font = pygame.font.SysFont('Kaisotai-Next-UP-B.ttf', size)
    text_surface = head_font.render(text, True, color)
    screen.blit(text_surface, pos)


class button():
    # 建立圖片按鈕
    def img(pos, text, color, bgcolor, size, line):
        x, y = pos
        dx, dy = size
        mX, mY = pygame.mouse.get_pos()

        if ((x < mX and mX < dx+x) and (y < mY and mY < dy+y)):
            pygame.draw.rect(screen, (255, 255, 255), [
                             x-line, y-line, dx+line*2, dy+line*2])
            pygame.draw.rect(screen, bgcolor, [x, y, dx, dy])
        else:
            pygame.draw.rect(screen, (0, 0, 0), [
                             x-line, y-line, dx+line*2, dy+line*2])
            pygame.draw.rect(screen, bgcolor, [x, y, dx, dy])
        # word(text,color,pos)
        screen.blit(text, pos)

    # 建立文字按鈕
    def text(pos, text, color, bgcolor, size, line, Fsize=60):
        x, y = pos
        dx, dy = size
        mX, mY = pygame.mouse.get_pos()

        if ((x < mX and mX < dx+x) and (y < mY and mY < dy+y)):
            pygame.draw.rect(screen, (255, 255, 255), [
                             x-line, y-line, dx+line*2, dy+line*2])
            pygame.draw.rect(screen, bgcolor, [x, y, dx, dy])
        else:
            pygame.draw.rect(screen, (0, 0, 0), [
                             x-line, y-line, dx+line*2, dy+line*2])
            pygame.draw.rect(screen, bgcolor, [x, y, dx, dy])
        word(text, color, pos, Fsize)

    def click(pos, text, color, bgcolor, size, line):
        x, y = pos
        dx, dy = size
        mX, mY = pygame.mouse.get_pos()

        if (event.type == pygame.MOUSEBUTTONDOWN and (x < mX and mX < dx+x) and (y < mY and mY < dy+y)):
            pygame.draw.rect(screen, (255, 0, 0), [x, y, dx, dy])
            print(text)
        else:
            pygame.draw.rect(screen, bgcolor, [x, y, dx, dy])
        # word(text,color,pos)
        screen.blit(text, pos)
        pygame.display.update()
        pygame.time.delay(10)


# 視窗名稱
pygame.display.set_caption('title')

# 背景色
screen.fill((40, 49, 158))


pygame.display.update()  # 更新頁面

while True:

    FuncPage(page)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
