## 右手法
## 進行方向を保持

######################

    # 0 : 通路
    # 1 : ゴール => 成功条件
    # 2 : 通過済みルート
    # 9 : 壁、通れないところ => 失敗条件

######################

maze = [
    [9,9,9,9,9,9,9,9,9,9,9,9],
    [9,0,0,0,9,0,0,0,0,0,0,9],
    [9,0,9,0,0,0,9,9,0,9,9,9],
    [9,0,9,9,0,9,0,0,0,9,0,9],
    [9,0,0,0,9,0,0,9,9,0,9,9],
    [9,9,9,0,0,9,0,9,0,0,0,9],
    [9,0,0,0,9,0,9,0,0,9,1,9],
    [9,0,9,0,0,0,0,9,0,0,9,9],
    [9,0,0,9,0,9,0,0,9,0,0,9],
    [9,0,9,0,9,0,9,0,0,9,0,9],
    [9,0,0,0,0,0,0,9,0,0,0,9],
    [9,9,9,9,9,9,9,9,9,9,9,9]
]


## 右手法での移動方向
dir = [[1,0],[0,1],[-1,0],[0,-1]]

## スタート地点(x座標、y座標、移動回数, 方向)をセット
x, y, depth, d = 1, 1, 0, 0

while maze[x][y] != 1:

    ## 探索済み座標をset
    maze[x][y] = 2

    ## 右手法での探索
    for i in range(len(dir)):
        
        ## 右方向をセット
        j = (d + i - 1) % len(dir) ## 移動方向の個数で割ったあまりは、次の方向を決める
        print("j = {}, d = {}, i = {}, len(dir) = {}".format(j, d, i, len(dir))) # j = 0, d = 0, i = 1, len(dir) = 4

        if maze[ x + dir[j][0] ][ y + dir[j][1] ] < 2: ## 通過済みかどうかチェック # maze[1+1][1+0] => 0
            ## 未訪問だった場合 => 進む. 移動回数を増やす
            print("進みます. d = {}".format(d))
            x += dir[j][0] # 2
            y += dir[j][1] # 1
            d = j # 0
            depth += 1 # 1
            break
        elif maze[ x + dir[j][0] ][ y + dir[j][1] ] == 2:
            ## 訪問済みの場合 => 進む. 移動回数を減らす
            print("もどります. d = {}".format(d))
            x += dir[j][0]
            y += dir[j][1]
            d = j
            depth -= 1
            break
        print("d = {}".format(d))

## ゴール到達
print("x = {}, y = {}, depth = {}, d = {}".format(x,y,depth,d))