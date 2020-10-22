## リスト内包表記 : ループと条件を使って、1行でリストを作成する方法
## 変数名 = [ 式 for 変数 in リスト (if 条件式)]

## 以下の2つは同義
# new_list = [ x for x in list_a ]

# new_list = []
# for x in list_a:
#     new_list.append(x)

## 2つめ
# new_list = [ x for x in list_a if type(x) == int]

# new_list = []
# for x in list_a:
#     if type(x) == int:
#        new_list.append(x)


list_a = (1,2,3,"a",4,"b") # タプル

# list_b = [x for x in list_a] # list_aのリスト. [1, 2, 3, 'a', 4, 'b']
# print(list_b)

# list_c = [x for x in list_a if type(x) == int] # int型の時のみ, xを返す [1, 2, 3,  4]
# print(list_c)

# list_d = [x for x in range(100) if x % 7 == 0] # int型の時のみ, xを返す [1, 2, 3,  4]
# print(list_d)

# dict_a = {
#     "a" : "apple",
#     "b" : "banana"
# }

# list_e = [dict_a.get(x) for x in list_a if type(x) == str] # ['apple', 'banana']
# print(list_e)

# list_x = tuple(x for x in range(100))
# print(type(list_x))


## 素数の取り出し
# def func(n):
#     for x in range(2,n):
#         if n % x == 0:
#             return True
#     return False

# list_z = [ x for x in range(100) if func(x) == False]
# print(list_z)