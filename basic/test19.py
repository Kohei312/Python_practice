## enumerate関数, zip関数

### enumerate(変数) : 引数内の変数(配列)中の値, indexを同時に取得できる処理
# sam = ["A","B","C"]
# for index,value in enumerate(sam):
#     print(index) # 0,1,2
#     print(value) # A, B, C


### zip(変数, 変数) : 引数内の2つの変数(配列)内の値を、同時に取得する処理
### 配列内の要素数が異なる場合は、少ないほうの数にあわせてループする
list_1 = ["A","B"]
list_2 = ["D","E","F"]

for a,b in zip(list_1,list_2):
    print(a) # A, B
    print(b) # D, E