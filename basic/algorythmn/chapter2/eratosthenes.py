## エラトステネスのふるい
## nの倍数ずつ除外していく

import math

def get_prime(x):   
    
    prime = [] ## 素数のリスト.

    if x <= 1:
        return []
    elif x % 2 == 0:
        prime.append(2) ## 2で割れたら代入 => 以降, 2の倍数である偶数は計算対象から弾くことができる
    
    limit = int(math.sqrt(x)) ## 対象値の平方根 => 検索最大値

    ## 奇数のリストを作成
    data = [i + 1 for i in range(2, x, 2) ]

    while limit > data[0]: ## 奇数リストのうち、検索最大値までの範囲をループ => 平方根以下の数に素数があるかどうかで判別可能
        prime.append(data[0])
        # 割り切れない数だけ抽出
        data = [ j for j in data if j % data[0] != 0 ]
    return prime + data

print(get_prime(200))