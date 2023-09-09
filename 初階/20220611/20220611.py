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
    HP = random.randint(0, 1)
    print('角色獲得{}點HP'.format(HP))
    s[1] += HP


def update_money(s):
    Money = random.randint(10, 30)
    print('角色獲得{}塊錢'.format(Money))
    s[2] += Money


def fighting(s):
    t = 0.5
    m_HP = random.randint(2, 10)
    print('monster life{}'.format(m_HP))

    while True:
        attack = random.randint(1, 3)
        print('You make damage'.format(attack))
        m_HP -= attack
        time.sleep(t)
        print('monster life{}'.format(m_HP))

        if (m_HP < 1):
            print('You beat monster')
            s[2] += random.randint(10, 20)
            break
        else:
            print('monster attack')
            s[1] -= 1
            time.sleep(t)
            print('you hurt, life = {}'.format(s[1]))
            if (s[1] < 1):
                print('you dead')
                s[0] = 0
                break


file = 'save.txt'
status = []
try:
    f = open(file, 'r')
except:
    status = [1, 10, 0]
else:
    for line in f:
        status.append(int(line))
    f.close()

print('角色目前狀態:HP = {},;Money = {}'.format(status[1], status[2]))
event = [update_life, update_money, fighting]

while True:
    ans = input('是否繼續?y or n')
    if (ans == 'y'):
        event[random.randrange(0, len(event))](status)
        print('角色目前狀態:HP = {},;Money = {}'.format(status[1], status[2]))
        if status[0] == 0:
            print('gameover')
            if status[2] >= 50:
                ans = input('是否購買生命藥水?')
                if ans == 'n':
                    status[0] = 1
                    status[1] = 10
                    status[2] = 50
                    for i in range(10):
                        print('復活進度:' + str(i * 10) + '%', end='\r')
                        time.sleep(0.5)
    else:
        print('遜!')
        file = 'save.txt'
        f = open(file, 'w')
        for i in status:
            f.write(str(i) + '\n')
        f.close()
        break
