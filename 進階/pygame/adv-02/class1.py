######################匯入模組######################
import pygame
import sys
import math


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


######################初始化######################

pygame.init()
width = 640
height = 320

######################建立視窗及物件######################
screen = pygame.display.set_mode((width, height))  # 建立繪圖視窗
pygame.display.set_caption("...")

######################設定文字######################
# 取得字體
typeface = pygame.font.get_default_font()
# 設定字體和大小
font = pygame.font.Font(typeface, 24)
# 設定文字參數: 文字內容，是否開啟反鋸齒，文字顏色，背景顏色
title = font.render("Start", True, (0, 0, 0))
# 取得文字寬度
tit_w = title.get_width()
# 取得文字高度
tit_h = title.get_height()

######################建立畫布######################
bg = pygame.Surface((width, height))
bg.fill((255, 255, 255))  # 底色為白色

#圓形(畫布,顏色,圓心,半徑,線寬)
# pygame.draw.circle(bg, (0, 0, 225), (200, 100), 30, 0)

#矩形(畫布,顏色,[x,y,寬,高],線寬)
# pygame.draw.rect(bg, (0, 225, 0), [270, 130, 60, 40], 5)

#橢圓形(畫布,顏色,[x,y,寬,高],線寬)
# pygame.draw.ellipse(bg, (0, 246, 225), [200, 50, 200, 170], 0)

#線(畫布,顏色,起點,終點,線寬)
# pygame.draw.line(bg, (0, 0, 0), (220, 110), (300, 140), 3)
# pygame.draw.line(bg, (0, 0, 0), (200, 140), (220, 200), 3)

#多變形(畫布,顏色,[[x1,y1],[x2,y2],[x3,y3]],線寬)
# pygame.draw.polygon(bg, (100, 200, 45), [[100, 100], [0, 200], [200, 200]])

#弧形(畫布,顏色,[x,y,寬,高],起始角度,結束角度,現寬)
# pygame.draw.arc(bg, (255, 10, 0), [100, 100, 100, 50], math.radians(180),
#                 math.radians(0), 2)

######################循環偵測######################
paint = False
color = (255, 255, 255)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            pos = pygame.mouse.get_pos()
            if check_click(pos, 0, 0, tit_w, tit_h):
                # 圓形(畫布,顏色,圓心,半徑,線寬)
                pygame.draw.circle(bg, (0, 0, 225), (200, 100), 30, 0)

                # 矩形(畫布,顏色,[x,y,寬,高],線寬)
                pygame.draw.rect(bg, (0, 225, 0), [270, 130, 60, 40], 5)

                # 橢圓形(畫布,顏色,[x,y,寬,高],線寬)
                pygame.draw.ellipse(bg, (0, 246, 225), [200, 50, 200, 170], 0)

                # 線(畫布,顏色,起點,終點,線寬)
                pygame.draw.line(bg, (0, 0, 0), (220, 110), (300, 140), 3)
                pygame.draw.line(bg, (0, 0, 0), (200, 140), (220, 200), 3)

                # 多變形(畫布,顏色,[[x1,y1],[x2,y2],[x3,y3]],線寬)
                pygame.draw.polygon(bg, (100, 200, 45),
                                    [[100, 100], [0, 200], [200, 200]])

                # 弧形(畫布,顏色,[x,y,寬,高],起始角度,結束角度,現寬)
                pygame.draw.arc(bg, (255, 10, 0), [100, 100, 100, 50],
                                math.radians(180), math.radians(0), 2)
            else:
                if event.button == 1:
                    color = (255, 0, 0)
                if event.button == 3:
                    color = (255, 255, 255)
                print('click!!')
                print(pygame.mouse.get_pos())
                paint = not (paint)
    if paint:
        x, y = pygame.mouse.get_pos()
        pygame.draw.circle(bg, color, (x, y), 10, 0)

    screen.blit(bg, (0, 0))
    screen.blit(title, (0, 0))
    pygame.display.update()