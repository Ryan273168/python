######################匯入模組######################
import pygame
import os
import sys
import random


####################定義函式######################
def gophers_update():
    global tick, pos, score, times, hitsur, gophers_tick
    if tick > max_tick:
        new_pos = random.randint(0, 5)
        pos = pos6[new_pos]
        tick = 0
        times += 1
    else:
        tick += 1

    if hitsur == gophers2:
        if gophers_tick > gophers_max_tick:
            hitsur = gophers
            gophers_tick = 0
        else:
            gophers_tick += 1
    screen.blit(
        hitsur,
        (pos[0] - hitsur.get_width() / 2, pos[1] - hitsur.get_height() / 2))


def score_update():
    score_sur = score_font.render(str(score), False, RED)
    screen.blit(score_sur, (10, 10))


def times_update():
    times_sur = times_font.render(str(times), False, RED)
    screen.blit(times_sur, (bg_x - 50, 10))


def check_click(pos, x_min, y_min, x_max, y_max):
    """判斷滑鼠是否點擊在指定的區域內"""
    x_match = x_min < pos[0] < x_max
    y_match = y_min < pos[1] < y_max
    if x_match and y_match:
        return True
    else:
        return False


def game_over():
    screen.fill(BLACK)
    end_sur = score_font.render(f"Game over~ Your Score is :{score}", False,
                                RED)
    screen.blit(end_sur, (bg_x / 2 - end_sur.get_width() / 2,
                          bg_y / 2 - end_sur.get_height() / 2))


def mouse_update():
    global hammer, hammer_tick

    if hammer == ham1:
        if hammer_tick > hammer_max_tick:
            hammer = ham2
            hammer_tick = 0
        else:
            hammer_tick += 1

    screen.blit(hammer, (mouse_pos[0] - 15, mouse_pos[1] - 15))


####################初始化######################
os.chdir(sys.path[0])
pygame.init()
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
clock = pygame.time.Clock()
tick = 0
max_tick = 20
bg_img = "Gophers_BG_800x600.png"
bg = pygame.image.load(bg_img)

bg_x = bg.get_width()
bg_y = bg.get_height()
######################建立視窗######################
screen = pygame.display.set_mode([bg_x, bg_y])
pygame.display.set_caption("打地鼠")

######################地鼠物件######################
pos6 = [[195, 305], [400, 305], [610, 305], [195, 450], [400, 450], [610, 450]]

pos = pos6[0]
gophers = pygame.image.load("Gophers150.png")
gophers2 = pygame.image.load("Gophers2_150.png")
hitsur = gophers
gophers_tick = 0
gophers_max_tick = 5
######################聲音物件######################
pygame.mixer.music.load("hit.mp3")
######################分數物件######################
score = 0
typeface = pygame.font.get_default_font()
score_font = pygame.font.Font(typeface, 24)
######################滑鼠物件######################
pygame.mouse.set_visible(False)
ham1 = pygame.image.load("Hammer1.png")
ham2 = pygame.image.load("Hammer2.png")
hammer = ham2
hammer_tick = 0
hammer_max_tick = 5
######################次數物件######################
times = 0
times_max = 100
typeface = pygame.font.get_default_font()
times_font = pygame.font.Font(typeface, 24)
######################循環偵測######################
while True:
    clock.tick(-1)  # 設定每秒30幀執行
    mouse_pos = pygame.mouse.get_pos()
    # 取得事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            hammer = ham1

        if event.type == pygame.MOUSEBUTTONDOWN:
            if check_click(mouse_pos, pos[0] - 50, pos[1] - 50, pos[0] + 50,
                           pos[1] + 50):
                tick = max_tick + 1
                score += 1
                hitsur = gophers2
                pygame.mixer.music.play()

    if times >= times_max:
        game_over()

    else:
        screen.blit(bg, (0, 0))
        gophers_update()
        score_update()
        times_update()
        mouse_update()

    # 更新繪圖視窗
    pygame.display.update()