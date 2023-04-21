#!/usr/bin/python
# -*- coding: ISO-8859-1 -*-
import pygame
import random
import os
import sys
import math

try:
    import serial
except ImportError:
    os.system('pip install pyserial')
    import serial


with open('galagaState.txt', 'w') as f:
    f.write('galagaOpening\n')
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

setting={}
setting_proj=[]
if os.path.isfile('setting.txt')==False:
    with open('galagaState.txt', 'w') as f:
        f.write('galagaClosed\n')
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
                            #print(setting)
                            
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




FPS = 60
WIDTH = 1000
HEIGHT = 750

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First game")
clock = pygame.time.Clock()

background_img = pygame.image.load(os.path.join("img", "background.jpg")).convert()
player_img = pygame.image.load(os.path.join("img", "player.png")).convert()
player_mini_img = pygame.transform.scale(player_img, (25, 19))
player_mini_img.set_colorkey(BLACK)
pygame.display.set_icon(player_mini_img)
bullet_img = pygame.image.load(os.path.join("img", "bullet.png")).convert()
rock_imgs = []
for i in range(7):
    rock_imgs.append(pygame.image.load(os.path.join("img", f"rock{i}.png")).convert())

expl_anim = {}
expl_anim['lg'] = []
expl_anim['sm'] = []
expl_anim['player'] = []
for i in range(9):
    expl_img = pygame.image.load(os.path.join("img", f"expl{i}.png")).convert()
    expl_img.set_colorkey(BLACK)
    expl_anim['lg'].append(pygame.transform.scale(expl_img, (75, 75)))
    expl_anim['sm'].append(pygame.transform.scale(expl_img, (30, 30)))
    player_expl_img = pygame.image.load(
        os.path.join("img", f"player_expl{i}.png")).convert()
    player_expl_img.set_colorkey(BLACK)
    expl_anim['player'].append(player_expl_img)
power_imgs = {}
power_imgs['shield'] = pygame.image.load(
    os.path.join("img", "shield.png")).convert()
power_imgs['gun'] = pygame.image.load(os.path.join("img", "gun.png")).convert()

shoot_sound = pygame.mixer.Sound(os.path.join("sound", "shoot.mp3"))
gun_sound = pygame.mixer.Sound(os.path.join("sound", "pow1.wav"))
shield_sound = pygame.mixer.Sound(os.path.join("sound", "pow0.wav"))
die_sound = pygame.mixer.Sound(os.path.join("sound", "rumble.ogg"))
xp1 = pygame.mixer.Sound(os.path.join("sound", "expl0.mp3"))
xp2 = pygame.mixer.Sound(os.path.join("sound", "expl1.mp3"))
expl_sounds = [
    xp1, xp2
]
pygame.mixer.music.load(os.path.join("sound", "background.mp3"))
volume = 0.02
pygame.mixer.music.set_volume(volume+0.09)
shoot_sound.set_volume(volume)
gun_sound.set_volume(volume)
shield_sound.set_volume(volume)
die_sound.set_volume(volume)
xp1.set_volume(volume)
xp2.set_volume(volume)
font_name = pygame.font.match_font("arial")


def word(text,color,pos,size=60):
    head_font = pygame.font.SysFont('Kaisotai-Next-UP-B.ttf', size)
    text_surface = head_font.render(text, True, color)
    screen.blit(text_surface, pos)



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
        

    def click(pos,text,color,bgcolor,size,line):
        x,y=pos
        dx,dy=size
        mX,mY=pygame.mouse.get_pos()
        
        if(event.type == pygame.MOUSEBUTTONDOWN and (x<mX and mX<dx+x) and (y<mY and mY<dy+y)):
            pygame.draw.rect(screen,(255,0,0),[x,y,dx,dy])
            #print(text)
        else:
            pygame.draw.rect(screen,bgcolor,[x,y,dx,dy])
        #word(text,color,pos)
        screen.blit(text,pos) 
        pygame.display.update()
        pygame.time.delay(10)

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)


def new_rock():
    r = Rock()
    all_sprites.add(r)
    rocks.add(r)

def new_superrock():
    nr = Superrock()
    all_sprites.add(nr)
    superrocks.add(nr)


def draw_health(surf, hp, x, y):
    if hp < 0:
        hp = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (hp/100)*BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)


def draw_lives(surf, lives, img, x, y):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 32*i
        img_rect.y = y
        surf.blit(img, img_rect)


def draw_init():
    global setting
    global mcu_isOnline
    screen.blit(background_img, (0, 0))
    draw_text(screen, 'Galaga', 64, WIDTH/2, HEIGHT/4)
    
    #draw_text(screen, setting['Left']+' '+setting['Right']+' move , space to shoot', 22, WIDTH/2, HEIGHT/2)
    #draw_text(screen, setting['Forword']+' '+setting['Backword']+' volume control', 22, WIDTH/2, HEIGHT*3/5)
    #draw_text(screen, 'press to start', 18, WIDTH/2, HEIGHT*3/4)
    start_img=pygame.image.load('img/start_2.png')
    button.img((WIDTH/2-100, HEIGHT*3/4-50),start_img,(0,0,0),(0,0,0),(200,100),1)

    pygame.display.update()
    waiting = True
    while waiting:
        clock.tick(FPS)
        print(mcu())
        #mcu()
        #print(mcu_isOnline)

        if mcu_isOnline==False:
            connect_img=pygame.image.load('img/connecting.png')
        else:
            connect_img=pygame.image.load('img/connected.png')

        screen.blit(connect_img, (WIDTH/2-50, HEIGHT*1/2-25))
        pygame.display.update()
        if mcu_feedback_list[6]==-3 :
                waiting = False
                return False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True
            elif event.type == pygame.KEYDOWN:
                waiting = False
                return False


def pause():
    paused = True
    screen.fill(BLACK)
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                paused = False
        
        draw_text(screen, "Paused", 64, WIDTH/2, HEIGHT/4)
        draw_text(screen, "'Press' to continue", 22, WIDTH/2, HEIGHT/2)
        draw_text(screen, str(score), 18, WIDTH/2, 10)
        pygame.display.update()
        clock.tick(5)


def dead():
    deadd = True
    while deadd:
        screen.fill(BLACK)
        back_img = pygame.image.load('img/back.png')
        button.img((0,0),back_img,(0,255,255),(150,150,150),(150,50),1)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open('galagaState.txt', 'w') as f:
                    f.write('galagaClosed\n')
                    f.write(str(score))
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    deadd = False
            elif(event.type == pygame.MOUSEBUTTONDOWN):
                mX,mY=pygame.mouse.get_pos()
                #button.img((0,0),back_img,(0,255,255),(150,150,150),(150,50),1)
                if( (0<mX and mX<150) and (0<mY and mY<50) ):   
                    with open('galagaState.txt', 'w') as f:
                        f.write('galagaClosed\n')
                        f.write(str(score))

                    pygame.quit()
                    sys.exit()
        
        draw_text(screen, "Game Over", 64, WIDTH/2, HEIGHT/4)
        draw_text(screen, "'Press p' to continue", 22, WIDTH/2, HEIGHT*3/4)
        draw_text(screen, str(score), 18, WIDTH/2, HEIGHT/2)

        pygame.display.update()
        clock.tick(5)
    return True


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (50, 38))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 8
        self.health = 100
        self.lives = 3
        self.hidden = False
        self.hide_time = 0
        self.gun = 1
        self.gun_time = 0

    def update(self):
        now = pygame.time.get_ticks()
        if self.gun > 1 and now - self.gun_time > 5000:
            self.gun -= 1
            self.gun_time = now

        if self.hidden and now - self.hide_time > 1000:
            self.hidden = False
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 10

        key_pressed = pygame.key.get_pressed()
        if mcu_feedback_list[1]>=1:
            self.rect.x += self.speedx
        if mcu_feedback_list[1]<=-1:
            self.rect.x -= self.speedx

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        if not (self.hidden):
            if self.gun == 1:
                bullet = Bullet(self.rect.centerx, self.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
                shoot_sound.play()
            elif self.gun >= 2:
                bullet1 = Bullet(self.rect.left, self.rect.centery)
                bullet2 = Bullet(self.rect.right, self.rect.centery)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                bullets.add(bullet1)
                bullets.add(bullet2)
                shoot_sound.play()

    def hide(self):
        self.hidden = True
        self.hide_time = pygame.time.get_ticks()
        self.rect.center = (WIDTH/2, HEIGHT+500)

    def gunup(self):
        self.gun += 1
        self.gun_time = pygame.time.get_ticks()


class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_ori = random.choice(rock_imgs)
        self.image_ori.set_colorkey(BLACK)
        self.image = self.image_ori.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.85 / 2)
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-180, -100)
        self.speedy = random.randrange(a, b)
        self.speedx = random.randrange(c, d)
        self.total_degree = 0
        self.rot_degree = random.randrange(-3, 3)

    def rotate(self):
        self.total_degree += self.rot_degree
        self.total_degree = self.total_degree % 360
        self.image = pygame.transform.rotate(self.image_ori, self.total_degree)
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center

    def update(self):
        self.rotate()
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(2, 10)
            self.speedx = random.randrange(-3, 3)

class Superrock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_ori = random.choice(rock_imgs)
        self.image_ori.set_colorkey(BLACK)
        self.image = self.image_ori.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.85 / 2)
        x_list = [1, 2, 3, 4, 3/2, 10]
        self.rect.x = WIDTH/random.choice(x_list)
        self.rect.y = 0
        self.speedy = superrock_speedy
        self.speedx = superrock_speedx

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += math.sin(math.pi*(self.speedx)/180)*10
        self.speedx += 5
        if self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0:
            self.rect.x = WIDTH/2
            self.rect.y = -self.rect.height

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()


class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = expl_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(expl_anim[self.size]):
                self.kill()
            else:
                self.image = expl_anim[self.size][self.frame]
                center = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = center


class Power(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['shield', 'gun'])
        self.image = power_imgs[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 3

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.kill()


pygame.mixer.music.play(-1)

show_init = True
running = True
rock_num = 1
flag = 1
rax = 0
counter = 0
interval = 30

while running:
    mcu()
    if show_init:
        close = draw_init()
        dead1 = False
        a = 2
        b = 5
        c = -3
        d = 3
        superrock_speedx = 1
        superrock_speedy = 3
        rock_num = 1
        flag = 1
        rax = 0
        if close:
            break
        show_init = False
        all_sprites = pygame.sprite.Group()
        rocks = pygame.sprite.Group()
        superrocks = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        powers = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)
        for i in range(8):
            new_rock()
        score = 0

    if mcu_feedback_list[5]==0:
        player.shoot()
        mcu_feedback_list[5]=1
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.key.key_code(setting['Pause']):
                pause()
            if mcu_feedback_list[0]>=1:
                volume = min(volume + 0.05, 1)
                pygame.mixer.music.set_volume(volume)
                shoot_sound.set_volume(volume)
                gun_sound.set_volume(volume)
                shield_sound.set_volume(volume)
                die_sound.set_volume(volume)
                xp1.set_volume(volume)
                xp2.set_volume(volume)
            elif mcu_feedback_list[0]<=-1:
                volume = max(volume - 0.05, 0)
                pygame.mixer.music.set_volume(volume)
                shoot_sound.set_volume(volume)
                gun_sound.set_volume(volume)
                shield_sound.set_volume(volume)
                die_sound.set_volume(volume)
                xp1.set_volume(volume)
                xp2.set_volume(volume)

    all_sprites.update()

    hits = pygame.sprite.groupcollide(rocks, bullets, True, True)
    # rock_num = 1
    # flag = 1
    # rax = 0
    # counter = 0
    # interval = 30
    for hit in hits:
        random.choice(expl_sounds).play()
        score += hit.radius
        expl = Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)
        if random.random() > 0.9:
            pow = Power(hit.rect.center)
            all_sprites.add(pow)
            powers.add(pow)
        if flag % 2 == 0:
            for turn in range(rock_num+1):
                new_rock()
        flag += 1
        if flag % 30 == 0 and rax < 1:
            if counter < 5:
                if pygame.time.get_ticks() % interval == 0:
                    new_superrock()
                    counter += 1
            if counter == 5:
                rax += 1
        if flag % 60 == 0 and rax < 2:
            superrock_speedy = 6
            for superrock in range(3):
                new_superrock()
            rax += 1
        if flag % 120 == 0 and rax < 3:
            rock_num += 1
            a += 1
            b += 2
            rax += 1

    hits = pygame.sprite.groupcollide(superrocks, bullets, True, True)
    for hit in hits:
        random.choice(expl_sounds).play()
        score += hit.radius
        expl = Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)
        if random.random() > 0.9:
            pow = Power(hit.rect.center)
            all_sprites.add(pow)
            powers.add(pow)
        new_superrock()

    hits = pygame.sprite.spritecollide(
        player, rocks, True, pygame.sprite.collide_circle)
    for hit in hits:
        new_rock()
        player.health -= hit.radius * 2
        expl = Explosion(hit.rect.center, 'sm')
        all_sprites.add(expl)
        if player.health <= 0:
            death_expl = Explosion(player.rect.center, 'player')
            all_sprites.add(death_expl)
            die_sound.play()
            player.lives -= 1
            player.health = 100
            player.hide()
    
    hits = pygame.sprite.spritecollide(
        player, superrocks, True, pygame.sprite.collide_circle)
    for hit in hits:
        new_superrock()
        player.health -= hit.radius * 2
        expl = Explosion(hit.rect.center, 'sm')
        all_sprites.add(expl)
        if player.health <= 0:
            death_expl = Explosion(player.rect.center, 'player')
            all_sprites.add(death_expl)
            die_sound.play()
            player.lives -= 1
            player.health = 100
            player.hide()

    hits = pygame.sprite.spritecollide(player, powers, True)
    for hit in hits:
        if hit.type == 'shield':
            player.health += 20
            if player.health > 100:
                player.health = 100
            shield_sound.play()
        elif hit.type == 'gun':
            player.gunup()
            gun_sound.play()

    

    screen.fill(BLACK)
    screen.blit(background_img, (0, 0))
    all_sprites.draw(screen)
    draw_text(screen, str(score), 18, WIDTH/2, 10)
    draw_health(screen, player.health, 5, 15)
    draw_lives(screen, player.lives, player_mini_img, WIDTH - 100, 15)
    if player.lives == 0 and not (death_expl.alive()):
        show_init = dead()
    pygame.display.update()

with open('galagaState.txt', 'w') as f:
    f.write('galagaClosed\n')
    f.write(str(score))
pygame.quit()
