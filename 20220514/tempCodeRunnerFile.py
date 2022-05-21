i = []
while True:
    print("1.想加入菜單的果汁2.顯示出目前所有果汁3.離開系統")
    num = (input("請输入功能選項:"))
    if num == "1":
        menu = (input("請輸入想加入菜單的果汁"))
        if menu == menu:
            print("此果汁已列入清單中")
        else:
            i.append(menu)
    elif num == "2":
        print(i)
    elif num == "3":
        break
