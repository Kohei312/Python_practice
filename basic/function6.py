## サブジェネレータ関数
## 書き方：yield from

def sub_sub_generator():
    yield "sub sub のyield"
    return "sub sub のreturn"

def sub_generator():
    yield "sub のyield"
    res = yield from sub_sub_generator()
    print("res = {}".format(res))
    return "sub のreturn"

def generator():
    yield "generator のyield"
    res = yield from sub_generator()
    print("gen res = {}".format((res)))
    return "generatorのreturn"

gen  = generator()
print(next(gen)) # generator のyield
print(next(gen)) # sub のyield
print(next(gen)) # sub sub のyield
print(next(gen)) # res = sub sub のreturn,  gen res = sub のreturn, エラー
print(next(gen)) # 実行されず