## フィボナッチ数列 : 直前の2つの数字を足し合わせてできる数列.
## [ 1, 1, 2, 3, 5, 8, 13, 21, ...] のようになる.
## 最初の2つの数字は[1,1]

# ## メモ化 : 一度計算した値を保存し、再利用できる状態にする方法
# memo = {1:1 , 2:1} ## fibonacci() の 終了条件（辞書型. []でなく、{} で囲うことに注意）

# def fibonacci(n):
#     if n in memo:
#         return memo[n]
    
#     memo[n] = fibonacci(n-2) + fibonacci(n-1) 
#     return memo[n]

#     # if (n == 1) or (n == 2):
#     #     return 1  
#     # return fibonacci(n - 2) + fibonacci(n - 1)

# print(fibonacci(9))

def fibonacci(n):
    fib = [1,1]
    for i in range(2,n):
        fib.append(fib[i-2] + fib[i-1])

    return fib[n-1]

print(fibonacci(3))