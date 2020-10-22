## ヒープソート: 
## スタック（LIFO）、キュー（FIFO）のデータの取り扱い
## スタック：最新のものを、リストの最後に追加する（ = append ）。取り出すときは、配列の末尾のデータから取り出す ( = pop )
## キュー： 最新のものを、リストの最後に追加する（ = queue.Queue().put. エンキューという ）. 取り出すときは、配列の最初のデータから取り出す ( =  queue.Queue().get。デキューという )
## ** Pythonでは、queueライブラリをimportして使用する

data=[6,15,4,2,8,5,11,9,7,13]

## ヒープ
for i in range(len(data)):
    now = i
    # for j in range(1,len(data)):
    #     if (now > 0) and data[now] > data[(now -1) // 2]:
    ## 短縮すると...
    while (now > 0) and data[now] > data[(now -1) // 2]:
            print("まえのnow : {}".format(now))
            data[(now - 1) // 2], data[now] = data[now], data[(now - 1) // 2]
            now = (now - 1) // 2
            print("いまのnow : {},実行結果 : {}".format(now,data))

## print(data) => [15, 13, 11, 8, 9, 4, 5, 2, 7, 6]

## range(終点, 始点, ステップ) => 始点から終点の範囲を、ステップ刻みで進める
## =>ここでは、0から10の範囲を、-1刻みで進める（=最後から最初のインデックスに向かって進む）
for k in range(len(data),0,-1):
    ## 最後と最初の値を入れ替え. (インデックスは、len()-1 までである点に注意)
    data[k -1], data[0] = data[0], data[k - 1]

    ## 処理位置に、ヒープの先頭を指定
    j = 0

    ## 左下の子インデックスは、終点よりも小さい（=配列の範囲外ではない）
    ## かつ、並び替え後の左下の子の値のほうが、並び替え後に親となった値よりも大きいか
    # left_heep = ( ( (2*j + 1) < k - 1 ) and ( data[j] < data[2*j + 1]  ) )
    ## または、かつ、並び替え後の右下の子の値のほうが、並び替え後に親となった値よりも大きいか
    # right_heep = ( ( (2*j + 2) < k - 1) and ( data[j] < data[2*j + 2]  ) )

    ## 変数で分岐条件を定義しても異なる挙動をするため、直接入力
    while ( ( (2*j + 1) < k - 1 ) and ( data[j] < data[2*j + 1]  ) )  or  ( ( (2*j + 2) < k - 1) and ( data[j] < data[2*j + 2]  ) ):
        print("2*j+1 : {}".format(2*j+1))
        print("2*j+2 : {}".format(2*j+2))
         ## 右下の子インデックスは、終点と等しい（=インデックスが、配列の範囲外ではない）
        if (2*j + 2 == k - 1 ) or (data[ 2*j + 2 ] < data[ 2*j + 1 ]):
            ## 左下の値と、その親の値を交換
            data[j], data[2*j+1] = data[2*j+1], data[j]
            ## 左下に移動する
            j = 2*j + 1
        else:
            ## 右下の値と、その親の値を交換
            data[j], data[2*j+2] = data[2*j+2], data[j]
            ## 右下に移動する
            j = 2*j + 2

print(data)