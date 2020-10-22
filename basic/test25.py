## 再帰 : 関数から自分の関数を呼び出すこと（ループ処理となる確率高いため要注意!!）
### ex) フィボナッチ数列
### ある数字の順列があるとき、 1,2番目の値からは1, 3番目以上の値からは直前2つの数値の和を返す数列のこと

# def fib(n):
#     if n < 3:
#         return 1
#     else:
#         print(n) ## 5,4,3
#         return fib(n-1)

# fib(5) 


def fib(x):
    return 1 if x < 3 else fib(x-1) + fib(x-2)

for x in range(1,10):
    print(fib(x))