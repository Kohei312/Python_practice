## 2分探索 : 中央値よりも 前/後 を探索していく方法. 事前にリストの昇順/降順ソートが必要
## x = log2Y （対数）ベースで計算量が増えるため、計算量が大幅に増えるリスクが非常に少なくなる => O(log N)

## 線形探索の場合、指数関数的に増加するため、計算量が大幅に増えるリスクが高い.リストのソートは必要なし.


## 希望の値valが、リストデータa_listの何番目にあるかを探す
def binary_search(a_list,val):

    # 配列内のインデックスを整理する
    left = 0  # 探索する範囲の左端を設定.
    right = len(a_list) - 1 # 探索する範囲の右端を設定

    while left <= right:
        mid = (left + right) // 2 # 探索する範囲の中央を計算

        if a_list[mid] > val: ## もし中央値が希望の値より大きかったら
            right = mid -1 ## 中央値より右側は対象外 → 中央値より左側の範囲で探索する → 探索の右端を、中央値の直前の値に再設定する
        
        elif a_list[mid] < val:

            left = mid + 1
        
        else:    
            return mid
    
    return -1

a_list = [10,20,30,40,50,60,70,80,90]
print(binary_search(a_list,40))


