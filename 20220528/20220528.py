# def add_juce(a_list):
#     y = (input("請輸入想加入菜單的果汁:"))
#     if a_list.count(y) > 0:
#         print("此果汁已列入清單中")
#     else:
#         a_list.append(y)
#     return a_list

# def show_juice(a_list):
#     print(a_list)

# def remove_juice(a_list):
#     y = (input("請輸入想刪除的果汁:"))
#     if y in a_list :
#         a_list.remove(y)
#     return a_list

# op = [add_juce, show_juice]
# i = []
# while True:
#     print("1.想加入菜單的果汁\n2.顯示出目前所有果汁\n3.想從菜單中刪除的果汁\n4.離開系統\n")
#     num = (input("請输入功能選項:"))
#     if num == "4":
#         break
#     i = op[num - 1](i)
