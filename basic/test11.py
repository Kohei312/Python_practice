## 辞書型 （ [] ではなく、{} で記述する点に注意 ）
## 書き方: 変数名 = { 'キー名' : '値','キー名' : '値'・・・} 

car = { 'brand' : "Toyota", "model": "Prius", "year":2015, 1:100}

## 値の取り出し方
## その１: キー名を指定する。キー名は、[]内に記述する
# print(car['brand']) # 対象となるキー名がみつからない場合、エラーとなる
## その２: .get("キー名")を使用する
# print(car.get("brand")) # "Toyota"
# print(car.get(1)) # 100
# print(car.get("bran")) # 対象となるキー名が見つからない場合、Noneが返ってくる（nullみたいなもの？）
# print(car.get("hoge",404)) # 第二引数に、Noneだった場合に返ってくる要素を指定できる

# print(car.keys()) # キー名の一覧を返す. dict_keys(['brand', 'model', 'year'])
# print(car.values()) #　値の一覧を返す. dict_values(['Toyota', 'Prius', 2015])
# print(car.items()) # [キー名：値]の一覧を返す. dict_items([('brand', 'Toyota'), ('model', 'Prius'), ('year', 2015)])

# for key,value in car.items(): # ループ処理で、dict内のキー名、値の両方を指定することも可能
#     print("key = {}, value = {}".format(key,value)) #key = brand, value = Toyota  key = model, value = Prius  key = year, value = 2015
#     if key in car: 
#       print(car[key]) # 取り出されたkey に対応する valueが、順番に表示される



## update :  辞書型の値を追加、更新する
# car.update({"brand":"Lexus", "country":'Japan', "prefecture":"Tokyo"}) 
# print(car.items()) # dict_items([('brand', 'Lexus'), ('model', 'Prius'), ('year', 2015), (1, 100), ('country', 'Japan'), ('prefecture', 'Tokyo')])

## キー名を指定して、直接書き換えることも可能
# car["brand"] = 'Mazda'
# print(car)

## popitem :  末尾にある要素を、辞書内から取り出す。（python 3.7以前では、削除する値を指定できる点に注意）
## 辞書から取り出した値は、タプル型として別の変数に入れ込むことも可能
# value = car.popitem()
# print(value) # (1, 100)
# print(car.popitem(1)) # python 3.8以上では、エラー

## pop : 引数にキー名を指定して、特定の値を取り出す。
## 辞書から取り出した値は、タプル型として別の変数に入れ込むことも可能
# value = car.pop("brand")
# print(value) # Toyota
# print(car) # {'model': 'Prius', 'year': 2015, 1: 100}

## clear : 辞書内の値を全て削除し、辞書を空にする。
# car.clear()
# print(car) # {}

## del : 辞書そのものを削除する
# del car
# print(car) # エラー（carという変数自体が削除されているため。del以降、検索候補にも出てこない点もポイント）