## 3目ならべ + ミニマックス法
## ミニマックス法は相手が自分にとって最も不利になる手を指すと仮定して、最善の手を探す方法
## 相手の考えて次の手を打つ

import random

goal = [
    0b111000000,0b000111000,0b000000111,0b100100100,
    0b010010010,0b001001001,0b100010001,0b001010100
    ]

## 3つ並んだか判定
def check(player):
    for mask in goal:
        if player & mask == mask:
            return True
    return False

## ミニマックス法
def minimax(p1, p2, turn):
    if check(p2):
        if turn: ## 自分の手番のときは勝ち
            return 1
        else:
            return -1

    board = p1 | p2
    if board == 0b11111111:
        return 0

    w = [ i for i in range(9) if (board & (1 << i)) == 0]
    print([minimax(p2, p1 | ( 1 << i ), not turn) for i in w ])
    if turn: ## 自分の手番の時は、最小値を選ぶ
        return min([minimax(p2, p1 | ( 1 << i ), not turn) for i in w ])
    else: ## 相手の手番の時は、最大値を選ぶ
        return max([minimax(p2, p1 | ( 1 << i), not turn ) for i in w ])

## 交互に置く
def play(p1, p2, turn):
    if check(p2): ## 3つ並んでいたら終了
        print([ bin(p1), bin(p2) ])
        return
    
    board = p1 | p2
    if board == 0b11111111:
        print([bin(p1),bin(p2)])
        return 

    ## 置ける場所を探す    
    w = [ i for i in range(9) if (board & (1 << i)) == 0]
    # print(" w = {}".format(w))
    ## 各場所に置いたときの評価値を調べる
    r = [ minimax(p2, p1 | (1 << i), True) for i in w ]
    ## 評価値が最も高い場所を取得する
    j = w[r.index(max(r))]
    play(p2, p1 | (1 << j), not turn)

play(0, 0, True)

