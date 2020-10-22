## 挿入ソート
## → 整数済みのリストの部分に、新しい要素を追加後、再度整列するアルゴリズム
## 選択ソートよりも処理が効率的 & 高速. ただし昇順・降順の並べ変えは、選択ソートのほうが高速。

list_a = [1,5,6,3,4,2,9,8,7]
# num = 7

## 今回は昇順にソート

for i in range(1, len(list_a)): ## rangeのstartを 1以上にしないと、検索範囲が逸脱する

    ## 整列済みの対象は外す
    min_index = i
    print("i : {}".format(i))
    ## 入れ替え処理の範囲を、徐々に狭めていく
    while min_index > 0 and list_a[min_index] < list_a[min_index-1]:
        list_a[min_index-1],list_a[min_index] = list_a[min_index],list_a[min_index-1]
        min_index -= 1 
        print(list_a)

# print(list_a)
