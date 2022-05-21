import random

num_dice = int(input('輸入擲骰子的數'))
Ready = input('push any button to start')


def roll_dice(n):
    dice = []
    for i in range(n):
        dice.append(random.randint(1, 6))
    return dice


def who_is_winner(usr_list, cmp_list):
    usr_all = 0
    for i in range(len(usr_list)):
        usr_all += usr_list[i]
    cmp_all = 0
    for i in range(len(cmp_list)):
        cmp_all += cmp_list[i]
    if usr_all > cmp_all:
        print('user win')
    elif usr_all > cmp_all:
        print('computer win')
    elif usr_all > cmp_all:
        print('平手')


user = roll_dice(num_dice)
print('user result = {}'.format(user))
comp = roll_dice(num_dice)
print('comp result = {}'.format(comp))
who_is_winner(user, comp)
