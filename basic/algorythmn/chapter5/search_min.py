## 選択ソート : リストの中から最小の要素を選んで、前に移動する方法

## やり方 その１：先頭から要素を検索し、それまでの要素都h隠して小さい値があれば記録する

data = [6,15,4,2,8,5,11,9,7,13]

## 最小値のインデックスを格納する変数を保持
# min_num = 0
## →data内の要素数だけ繰り返したい
for j in range(len(data)):

    ## ループごとに、最小値インデックス（比較する値のインデックス）を更新
    min_num = j
    ## min_numからdataの個数 のインデックス内を検索する
    for i in range(j,len(data)):
        
        ## min_num番目の値 > i番目の値
        if data[min_num] > data[i]:
            min_num = i

    ## 最小値のインデックスを見つける
    # print(min_num)
    data[j],data[min_num] = data[min_num],data[j]
    print(data)