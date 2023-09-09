# a = int(input('你的上學時間為:'))
# b = int(input('你的下課時間為:'))
# print('你的上學時間為{}'.format(b - a))

# a = input('輸入值')
# (a + 10)**2
# (a - 2 // 10)
# a * 3 / 10

print('歡迎使用計算機\n說明:\n  1.(輸入數字)(輸入運算符號)(輸入數字)=(答案)\n  2.運算符號為(+、-、*、/)')
while True:
    x = int(input('輸入數字'))
    y = int(input('輸入數字'))
    z = input('輸入運算符號')
    if z == '+':
        print('{}+{}={}'.format(x, y, (x + y)))
    elif z == '-':
        print('{}-{}={}'.format(x, y, (x - y)))
    elif z == '*':
        print('{}*{}={}'.format(x, y, (x * y)))
    elif z == '/':
        if x % y == 0:
            print('{}/{}={}'.format(x, y, (x // y)))
        else:
            print('{}/{}={}'.format(x, y, (x / y)))
    else:
        print('錯誤!!')
        print('請重新輸入')
