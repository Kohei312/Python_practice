## Map関数
## リスト、辞書などループ可能な型の変数を第２引数を、第１引数に入れた関数に代入し、その結果を出力する関数
## map = map(関数, ループ可能な変数) # 関数(ループ可能な変数)の返り値

# list_a = [1,2,3,4,5]
# map_a = map(lambda  x: x * 2, list_a)

# for x in map_a:
#     print(x) # 2,4,6,8,10


# man = {
#     "name" : "Ichiro",
#     "age" : "18",
#     "country" : "Japan"
# }

# map_man = map(lambda x: x + ',' + man.get(x),man)
# for x in map_man:
#     print(x)

def calcurate(x,y,z):
    if z == "+":
        return x + y
    elif z == "-":
        return x - y

map_cal = map(calcurate,range(5), [3,3,3,3,3],["+","-","+","-"]) # 第1引数 = 処理する関数, 第2,3,4引数 = calcurateの引数x,y,zに代入する値
for x in map_cal:
    print(x)

