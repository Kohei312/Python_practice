## 線形探索2 : O(n) の処理（n回の比較検索が必要. 計算量 (n+1)/2）

def linear_search(a_list, value):
    for i in range(len(a_list)):
        if a_list[i] == value:
            return i
    
    return -1


ex_list = [1,2,3,4,5,6,7,8,9,0,10]
print(linear_search(ex_list,7))