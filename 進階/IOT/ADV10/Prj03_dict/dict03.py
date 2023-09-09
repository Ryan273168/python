d = {}
t = int(input('請輸入想新增的元素數量:'))
for i in range(t):
    print(f'第{i}個元素')
    k = input("請輸入名稱:")
    v = input("請輸入編號:")
    d[k] = v
    print(d)
for key, val in d.items():
    print(f'{key}:{val}')

r = input('請輸入想刪除的元素Key:')
d.pop(r)
print(d)

for key, val in d.items():
    print(f'{key}:{val}')