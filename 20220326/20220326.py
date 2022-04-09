from email.errors import StartBoundaryNotFoundDefect

ans = input("請輸入你的姓名 :")
print("你的姓名是" + ans)
age = int(input("請輸入你的年齡 : "))
if age >= 10:
    print("你還蠻大的")
else:
    print("兒童不宜，請立刻離開")
high = int(input("請輸入你的身高 :"))
if high <= 130:
    print("哈哈!矮冬瓜")
else:
    print("聽你這麼一說，你很勇嗎")
year = int(input("請輸入今年是多少年 :"))
if year == 2022:
    print("不錯")
else:
    print("看看右下角，阿呆")
wether = int(input("請輸入今天的天氣,晴天按1、雨天按2 :"))
if wether == 1:
    print("今天天氣不錯")
elif wether == 2:
    print("笑你不能出門")