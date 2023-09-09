######################匯入模組######################
import pygame
import sys
import math
######################初始化######################

pygame.init()
width = 640
height = 320

######################建立視窗及物件######################
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("...")

######################建立畫布######################
bg = pygame.Surface((width, height))
bg.fill((255, 255, 255))

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
    pygame.display.update()