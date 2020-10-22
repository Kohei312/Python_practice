## バブルソート：リストの隣り合ったデータを比較して、大小の順序が違っているときは並べ替えていく方法です

data=[6,15,4,2,8,5,11,9,7,1]

## スタート地点を設定
for j in range(0,len(data)):

    ## スタート地点のインデックスから順番に、隣り合う要素を比較していく
    ## 比較範囲は、dataの総個数 - (比較インデックス+1 分の値の個数 = 計算後の値の個数)
    for i in range(0,len(data)-(j+1)):
        print("i :{}".format(i))
        print("len(data)-j :{}".format(len(data)-j))
        if data[i] > data[i+1]:
            data[i], data[i+1] = data[i+1], data[i]
            print(data)

    # for i in range(len(data)-j - 1):
    #     if data[i] > data[i + 1]:
    #         data[i], data[i+1] = data[i+1], data[i]
    #         print(data)