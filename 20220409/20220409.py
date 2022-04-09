# bool() ()判斷()內是否有東西
# int() 變成整數
#float() 變成小數
#str() 變成字串
#round() 四捨五入
#import matplot匯入模組
#運算元:進行運算的資料
#運算子:進行運算的方法
# 二元運算子:加法 + 減法- 乘法* 小數除法 / 整數除法// 取餘數% 次方**
# ans = int(input("請輸入元的半徑:"))
# print(ans * ans * 3.14)
import matplotlib

print("OK")

import matplotlib.pyplot as plt
import matplotlib.image as img

image = img.imread("20220409/th.jpg")
plt.imshow(image)
plt.show()