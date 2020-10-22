## list, generator

## メモリ確認できるライブラリ
import sys

list_a = [i for i in range(100000)]

## 何百万ものデータを繰り返し処理する場合は、generatorで処理するほうがメモリ使用量を節約できて効率的
## 100データくらいでも節約にはなる.
def num(max):
    i = 0
    while i < max:
        yield i
        i += 1
gen = num(100000)

## ジェネレータでは、以下と同じ処理を行っている。違うのは、メモリ使用量.
# for i in list_a:
#     print(i)

## 10万件の繰り返し処理をしたとき
print(sys.getsizeof(list_a)) # 824456(バイト)
print(sys.getsizeof(gen)) # 112(バイト)

## 100件の繰り返し処理をしたとき
print(sys.getsizeof(list_a)) # 904(バイト)
print(sys.getsizeof(gen)) # 112(バイト)