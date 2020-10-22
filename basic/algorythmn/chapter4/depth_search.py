## ⇆ 深さ優先探索 : 特定の要素を掘り下げるだけ掘り下げて、進めなくなったらもどる方法（使用場面 : オセロなどの対戦型ゲーム）

## 行きがけ順 : 各ノードの子を辿る前に、そのノードを処理する
tree = [ [1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14],[],[],[],[],[],[],[],[],[] ]

def search(pos):
    print(pos, end=' ') # 配下のノードを調べる前に出力

    for i in tree[pos]:
        search(i)

search(0)

# 0 : tree[0]へ => 1
## 1 : tree[1]へ => 3
### 3 : tree[3]へ => 7 
#### 7 → 空. 終了
#### 8 → 空. 終了
### 4 : tree[4]へ => 9
#### 9 → 空. 終了
#### 10 → 空. 終了
## 2 : tree[2]へ => 5 
### 5 : tree[5]へ => 11 
#### 11 → 空. 終了
#### 12 → 空. 終了
### 6 : tree[6]へ => 13
#### 13 → 空. 終了
#### 14 → 空. 終了