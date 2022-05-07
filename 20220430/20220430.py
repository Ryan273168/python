# import random
# print(random.randrange(1, 7))

# import random
# print(random.randint(1, 6))

# X = int(input("請输入一个数字:"))
# sum = 0
# i = 0
# while i <= X:
#     sum += i
#     i += 1
#     print(sum)

# i = 1
# while i < 6:
#     if i == 3:
#         break
#     print(i)
#     i += 1
# else:
#     print("正常結束")

# while True:
#     num = (input("請输入果汁編號:"))
#     if num == "1":
#         print("你的商品是:蘋果汁")
#     elif num == "2":
#         print("你的商品是:柳橙汁")
#     elif num == "3":
#         print("你的商品是:葡萄汁")
#     elif num == "4":
#         break
#     else:
#         print("!!!輸入錯誤查無此果汁!!!")

# import turtle

# turtle.penup()
# turtle.speed(0)

# for i in range(8):
#     turtle.right(45 * i)
#     turtle.forward(100)
#     turtle.stamp()
#     turtle.home()

# turtle.done()

import turtle
import time

turtle.pendown()
turtle.speed(0)

for i in range(60):
    for j in range(12):
        turtle.penup()
        turtle.right(j * 30)
        turtle.forward(100)
        turtle.stamp()
        turtle.home()
    turtle.pendown()
    turtle.right(i * 6)
    turtle.forward(100)
    turtle.home()
    time.sleep(1)
    turtle.clear()

turtle.done()
