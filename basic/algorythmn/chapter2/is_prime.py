## 素数かどうかを判定する

## 対象数の平方根を求める ← 平方根の値までの範囲で、割り切れる数字があれば素数と判定可能（エラトステネスの篩）

import math

# print("x :  {}".format(x)) ## 2.449489742783178
# print(type(x)) ## float

def is_prime(x):
    if x <= 1:
        return False

    for i in range(2, int(math.sqrt(x))+1): # 2から開始し、( xの整数値(int(x))-1 ) +1 までの範囲をループする.(ループ最終点の値は、ループ制御文内では使用されないため +1 で補正) 
        if x % i == 0:
            return False    
    return True

for j in range(200):
    if is_prime(j):
        print(j, end=' ')





