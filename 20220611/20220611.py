# 初始血量:10
# 初始錢:0元
# 冒險者攻擊力:1-3
# 怪物攻擊力:1點
# 獲得紅藥水:1-3點
# 錢袋:10-30
# 擊敗怪物可得到10-20元
# 回合制，冒險者有優先攻擊權
# 冒險者隨機對怪物產生1-3點傷害
# 怪物生命隨機2-10點，攻擊1點
# 戰鬥結束後更新冒險者狀態
import random
import time


def update_life(s):
    HP = random.randint(1, 3)
    print('角色獲得{}點HP'.format(HP))
    s[1] += HP


def update_money(s):
    Money = random.randint(10, 30)
    print('角色獲得{}塊錢'.format(Money))
    s[2] += Money


def fighting(s):
    m_life = random.randint
    m_atk = random.randint


status = [1, 10, 0]
event = [update_life, update_money, fighting]

while True:
    ans = input('是否繼續?y or n')
    if (ans == 'y'):
        event[random.randrange(0, len(event))](status)
        print('角色目前狀態:HP = {},;Money = {}'.format(status[1], status[2]))
    else:
        print('遜!')
        break
