# .split("")分割字串
# EX:1,2,3>>['1','2','3']
# ans = input("請輸入一段文字")
# print(ans.split(','))

# ' '.join()重組字串
# img = ["I", "am", "tea"]
# s_img = ' '.join(img)
# print('{} type = {}'.format(s_img, type(s_img)))

# list()轉換型態
# print(list('a'))

# 取對應位置數值  從0開始
# i = ["a", "b", "c"]
# print(i[1])

# 改變清單數值
# i = ["a", "b", "c"]
# print(i)
# i[0] = 'A'
# print(i)

# .append( )加入資料在最後方
# i = [1, 2, 3]
# i.append(4)
# print(i)

# .remove()移除元素
# i = ['a','b','c']
# i.remove('a')
# print(i)

# .insert()插入指定的位置
# i = ['a', 'b', 'c']
# i.insert(0, 'A')
# print(i)

# .pop()移除最後或指定元素
# i = ['1', '2']
# i.pop()
# print(i)

# .sort()由小到大排列
# i = ['3', '1', '2']
# i.sort()
# print(i)

# .reverse()直接顛倒排列
# i = ['1', '2', '3']
# i.reverse()
# print(i)

# .index找出元素順序 從左到右
# i = ['a', 'b', 'c']
# index = i.index('a')
# print(index)

while True:
    print("1.想加入菜單的果汁2.顯示出目前所有果汁3.離開系統")
    i = []
    num = (input("請输入功能選項:"))
    if num == "1":
        menu = i.append(input("請輸入想加入菜單的果汁"))
    elif num == "2":
        print(i)
    elif num == "3":
        break