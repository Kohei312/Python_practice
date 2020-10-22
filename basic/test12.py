## タプル型
## 特徴：辞書型と違って、値を更新することはできない。特定の値にアクセスすることはできる
## →固定値を扱う際に便利。アクセススピードが辞書型より早い

fruit = ("apple",'grape')
fruit = fruit+ ('banana',) 
# print(fruit) # ('apple', 'grape', 'banana')

# fruit[0] = "hoge" # エラー
# print(fruit[0]) # "apple"

## 辞書型 ⇆ タプル型　の変換
# list_fruit = list(fruit)
# print(list_fruit)
# tuple_fruit = tuple(list_fruit)
# print(tuple_fruit)

## よくあるtuple活用例
pos = (135, 35)
countries = {pos : "Japan"}
## tuple型で辞書型のキーを指定し、値を取り出す操作が可能。キーは固定値で変更されない、アクセスが早くなる。
print(countries.get((135,35)))