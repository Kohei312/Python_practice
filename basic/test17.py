## all,any関数
### all : オブジェクトの中身がすべてTrueの場合に処理をする.条件分岐の結果もそのまま記述できる
# if all("反復可能なオブジェクト"): # ex) リスト, タプル, セットなど。for in でループ処理できる変数が対象
#   処理実行

### any : オブジェクトの1つでもTrueの場合に処理をする.条件分岐の結果もそのまま記述できる
# if any("反復可能なオブジェクト"):
#   処理実行

tup = (30<10, 10<20,"a" == "a")
if all(tup):
    print("all実行中")
elif any(tup):
    print("any実行中")

tup2 = (30<10, 10<5,"a" == "b")
if all(tup2):
    print("all実行中")
elif not any(tup2):
    print("any実行中")