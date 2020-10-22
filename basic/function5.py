## ジェネレータ関数
## 参考URL : https://qiita.com/keitakurita/items/5a31b902db6adfa45a70

## 使い道 : メモリを膨大に食う配列と違って、メモリ使用量を削減できる(大規模データ処理で大量にメモリを使用されることを避けることができる)
## ただし、処理速度は配列よりも遅くなる点はトレードオフ

## 書き方
# def func():
#     yield 戻り値

### yieldと記載した箇所で処理が停止し、戻り値が返される。

def generator(max):
    print("generator作成")

    for n in range(max):
        yield n
        print("yield実行")

gen = generator(10) # ここでは、まだ処理は実行されていない
# n = next(gen) # next(defのインスタンス)を記述すると、generator内のyieldまで処理が実行される
# print("n = {}".format(n)) # 0 ← yieldで返された値が出力される
# n = next(gen) # next(defのインスタンス)を記述すると、generator内のyieldから処理が再開される.
# print("n = {}".format(n)) # 1 ← yieldで返された値が出力される


## next()を省略する方法
# for x in gen:
#     print("x = {}".format(x))

## send

def generator2(max):
    print("generator2作成")

    for n in range(max):
        try:
          x = yield n # send使用時には、ここの書き方が変わる
          print("x = {}".format(x))
          print("yield実行")
        except ValueError as e:
          print("valueErrorです")

gen = generator2(10) ## ここでは、まだ処理は実行されていない
next(gen)
gen.send(100) ## yieldに記述した x に, 100という値を渡してgenerator2の処理を継続させている
gen.throw(ValueError("エラーです")) ## 無理やりexcept内の処理を呼び出す
gen.close() ## ここでgenerator2の処理が強制終了される 

# next(gen) ## →generator2は処理を停止しているため、再稼働しようにも動けない. 再度、generator2のインスタンスを定義する必要がある.