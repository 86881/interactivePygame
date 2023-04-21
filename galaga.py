import pygame
import random
import os
import sys
import math


with open('galagaState.txt', 'w') as f:
    f.write('galagaOpening\n')
    f.write('0\n')

setting = {}
setting_proj = []
if os.path.isfile('setting.txt') == False:
    with open('galagaState.txt', 'w') as f:
        f.write('galagaClosed\n')
        f.write('Without Setting!\n')
else:
    with open('setting.txt', 'r') as f:
        lineCount = 0

        for line in f:
            lineCount += 1
            line = line.replace("\n", "")
            line = line.replace("{", "")
            line = line.replace("}", "")
            line = line.replace("'", "")
            line = line.replace(",", "")

            if lineCount != 1:
                line = line.split(':')
                if len(line) == 2:
                    line[0], line[1] = line[0].replace(
                        ",", ''), line[1].replace(",", '')
                    line[0], line[1] = line[0].replace(
                        "\n", ''), line[1].replace("\n", '')
                    setting[line[0]] = line[1]
                    setting_proj.append(line[0])
                    # print(setting)


FPS = 60
WIDTH = 1000
HEIGHT = 750

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GAlaGA")
clock = pygame.time.Clock()

background_img = pygame.image.load(
    os.path.join("img", "background.jpg")).convert()
player_img = pygame.image.load(os.path.join("img", "player.png")).convert()
player_mini_img = pygame.transform.scale(player_img, (25, 19))
player_mini_img.set_colorkey(BLACK)
pygame.display.set_icon(player_mini_img)
bullet_img = pygame.image.load(os.path.join("img", "bullet.png")).convert()
rock_imgs = []
for i in range(7):
    rock_imgs.append(pygame.image.load(
        os.path.join("img", f"rock{i}.png")).convert())
#各類型圖片載入
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

#音效載入
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


def word(text, color, pos, size=60):
    head_font = pygame.font.SysFont('Kaisotai-Next-UP-B.ttf', size)
    text_surface = head_font.render(text, True, color)
    screen.blit(text_surface, pos)


class button():

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


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)

#創建新石頭
def new_rock():
    r = Rock()
    all_sprites.add(r)
    rocks.add(r)

#創建新特殊石頭
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

#載入初始頁面
def draw_init():
    global setting
    screen.blit(background_img, (0, 0))
    draw_text(screen, 'Galaga', 64, WIDTH/2, HEIGHT/4)
    draw_text(screen, setting['Left']+' '+setting['Right'] +
              ' move , space to shoot', 22, WIDTH/2, HEIGHT/2)
    draw_text(screen, setting['Forword']+' '+setting['Backword'] +
              ' volume control', 22, WIDTH/2, HEIGHT*3/5)
    draw_text(screen, 'press to start', 18, WIDTH/2, HEIGHT*3/4)

    pygame.display.update()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True
            elif event.type == pygame.KEYDOWN:
                waiting = False
                return False

#暫停頁面
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

#死亡頁面
def dead():
    deadd = True
    while deadd:
        screen.fill(BLACK)
        back_img = pygame.image.load('img/back.png')
        button.img((0, 0), back_img, (0, 255, 255),
                   (150, 150, 150), (150, 50), 1)

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
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                mX, mY = pygame.mouse.get_pos()
                # button.img((0,0),back_img,(0,255,255),(150,150,150),(150,50),1)
                if ((0 < mX and mX < 150) and (0 < mY and mY < 50)):
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

#玩家的程式碼
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
        if key_pressed[pygame.key.key_code(setting['Right'])]:
            self.rect.x += self.speedx
        if key_pressed[pygame.key.key_code(setting['Left'])]:
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

#石頭的程式碼
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

#特殊石頭的程式碼
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

#子彈的程式碼
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

#爆炸特效的程式碼
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

#各種buff的程式碼
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

#主程式
while running:
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
    #音量調節
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.key.key_code(setting['Shoot']):
                player.shoot()
            if event.key == pygame.key.key_code(setting['Pause']):
                pause()
            if event.key == setting['Forword']:
                volume = min(volume + 0.05, 1)
                pygame.mixer.music.set_volume(volume)
                shoot_sound.set_volume(volume)
                gun_sound.set_volume(volume)
                shield_sound.set_volume(volume)
                die_sound.set_volume(volume)
                xp1.set_volume(volume)
                xp2.set_volume(volume)
            elif event.key == setting['Backword']:
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
    #控制遊戲難度及子彈與石頭碰撞的結果
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
    #特殊石頭核子彈碰撞的結果
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
    #玩家和石頭碰撞的結果
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
    #玩家和特殊石頭碰撞的結果
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
    #玩家接觸buff時的結果
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
