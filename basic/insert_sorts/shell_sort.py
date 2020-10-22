## シェルソート
## 挿入ソートの改良版.
## →あらかじめ離れている要素を交換しておいて、最後に挿入ソートを実行する

## h- ソートの h の数は、最終的に1になるよう調整すればOK

list_a = [1,5,6,3,4,2,9,8,7]

def shellsort():
    h = len(list_a) // 2
    while h > 0: ## h = 0 となったら終了. list_a をリターンする 
        for i in range(h, len(list_a)): ## ここは比較対象となるindexを指定する. 開始範囲は、hから.
            
            # h = h_length // 2
            left = i 
            print("left : {}, h : {}".format(left, h))


            ## h- ソート実行
            while left > h and list_a[left - h] > list_a[left]:
                list_a[left], list_a[left - h] = list_a[left - h], list_a[left]
                left -= h
                print(list_a)

        h //= 2
        print("h // 2 : {}".format(h))

    return list_a
                

print(shellsort())