## 選択ソート
## →最小値(最大値)を選んで並び替えて整列する

# list_a = [1,5,5,6,5,4,2,1,8]

# # list_aの長さ -1 だけループ 8
# for i in range(len(list_a)):

#     # min_idx : i以上のインデックスで、最小値の入っているインデックス
#     min_idx = i

#     # j : i+1からスタート => list_aの長さ -1
#     for j in range(i+1, len(list_a)):

#         # 対象値が、以降の値よりも大きいかどうか
#         if list_a[min_idx] > list_a[j]:
#             # 対象値 > 以降の値 の場合は、値を更新する
#             min_idx = j
        
#     # 値の入れ替え
#     list_a[i], list_a[min_idx] = list_a[min_idx],list_a[i]
    
# print(list_a)


list_a = [1,5,7,6,3,4,2,9,8]

## リスト内の値を検索する
for i in range(len(list_a) -1):

    ## 比較対象の数
    min_index = i

    ## 全ての数字と比較し、最小値を探す
    for j in range(i+1, len(list_a)): ## rangeのend値未満までの整数値を検索している
        print("i :{}, j : {}, end : {}".format(i,j,len(list_a)))
        if list_a[j] < list_a[min_index]:
            min_index = j

    ## 検索後、比較対象数と最小値を交換する
    list_a[i],list_a[min_index] = list_a[min_index],list_a[i]    
    # print("list_a : {}".format(list_a))

