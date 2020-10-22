## 挿入ソート : ソート済みのリストに、追加するデータを先頭から順に比較し、格納する位置を見つけて追加する方法です。

## データをセット
data = [6,15,4,2,8,5,11,9,7,13]


for i in range(1, len(data)):

    ## 最小値の一時保存
    temp = data[i]
    
    ## ソート済みの左側グループ（比較対象となるグループ）を定義
    ## 比較対象となる基準値インデックス
    j = i - 1
    print("data[j] :{}, temp :{}".format(data[j], temp))
    
    ## pythonでは、j >= 0 は、「現在のjの値から、0までの範囲を降順にループするよ」の意味
    ##  → j >= 0を、for i in range(j,0) のような書き方にはできない
    while(j>=0) and (data[j]>temp):
            print("j :{}".format(j))
            ## 左側グループの端を、ひとつ後ろにずらす  
            data[j + 1] = data[j]
            j -= 1
            print("移行前:{}".format(data))
    ## ループを抜けたときに、差し込む値を
    data[j+1] = temp
    print("移行あと:{}".format(data))

