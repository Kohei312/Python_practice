## 番兵 : 終了条件としてリストの最後に付加するデータのこと
## →迷路の例だと、迷路の外堀を埋める 9 の壁が該当する.

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

def search(x,y,depth):

    if maze[x][y] == 1:
        print(depth)

    maze[x][y] = 2

    if maze[x][y-1] < 2:
        search(x,y-1,depth +1)

    if maze[x][y+1] < 2:
        search(x,y+1,depth +1)

    if maze[x-1][y] < 2:
        search(x-1,y,depth +1)
                    
    if maze[x+1][y] < 2:
        search(x+1,y,depth +1)
    
    maze[x][y] = 0 ## 行き止まりに当たったとき、スタート地点に戻る処理

search(1,1,0)