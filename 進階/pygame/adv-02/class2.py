######################匯入模組######################
import pygame
import sys
import os


####################定義函式######################
def check_click(pos, x_min, y_min, x_max, y_max):
    """判斷滑鼠是否點擊在指定的區域內"""
    # x_match = pos[0] > x_min and pos[0] < x_max
    x_match = x_min < pos[0] < x_max
    # y_match = pos[1] > y_min and pos[1] < y_max
    y_match = y_min < pos[1] < y_max
    if x_match and y_match:
        return True
    else:
        return False


####################初始化######################
os.chdir(sys.path[0])
pygame.init()
bg_img = "snow.jpg"
bg = pygame.image.load(bg_img)

bg_x = bg.get_width()
bg_y = bg.get_height()
######################建立視窗######################
screen = pygame.display.set_mode((bg_x, bg_y))
pygame.display.set_caption("Snow")
screen.blit(bg, (0, 0))
####################撥放音樂######################

####################設定文字######################
# 取得字體
typeface = pygame.font.get_default_font()
# 設定字體和大小
font = pygame.font.Font(typeface, 24)
titname = "Start"
# 設定文字參數: 文字內容，是否開啟反鋸齒，文字顏色，背景顏色
title = font.render(titname, True, (0, 0, 0))
# 取得文字寬度
tit_w = title.get_width()
# 取得文字高度
tit_h = title.get_height()
####################設定雪花基本參數######################

####################新增fps######################
clock = pygame.time.Clock
######################循環偵測######################
color = (255, 255, 255)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if check_click(pos, 0, 0, tit_w, tit_h):
                if titname == "Start":
                    titname = "Stop"
                else:
                    titname = "Start"

            title = font.render(titname, True, (0, 0, 0))

    screen.blit(bg, (0, 0))
    screen.blit(title, (0, 0))
    pygame.display.update()