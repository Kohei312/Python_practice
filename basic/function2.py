## 関数その2 ~ デフォルト値、複数の返り値

## デフォルト値は、引数内で 引数 = 値 のように記述
# def sam(arg1, arg2 = 100):
#     print(arg1, arg2) # 100 100

# sam(100)

## 可変長引数 : 引数に *をつけて、型を指定
## 引数が複数ある場合は、可変長引数は最後に記述する.
## 同じ可変長引数は、1つのみ記述可能.(複数記述すると、可変長引数の切れ目が判断できなくなる) 

### 可変長タプル型 : *変数
# def spam(arg1, *arg2):
#     print(arg1, arg2) # 1 (2, 3, 4, 5)
#     print(type(arg2)) # <class 'tuple'>
# spam(1,2,3,4,5)

### 可変長辞書型 : **変数
# def spam_2(arg1, **arg2):
#     print(arg1, arg2) # 1 {'name': 2, 'value': 3}
#     print(type(arg2)) # <class 'dict'>
# spam_2(1,name=2,value=3)

## →ただし、タプル型・辞書型を並行して1つずつ使うことはできる
# def spam_3(arg1, *arg2, **arg3):
#     print(arg1, arg2, arg3) # 1 (2, 3, 4, 5) {'name': 2, 'value': 3}
    
# spam_3(1,2,3,4,5,name=2,value=3)



## 複数の返り値
# def sam2():
#     return 1,2,3

# a,b,c = sam2()
# print(a,b,c)