## 演習: じゃんけん

## 相手の手を指定するループ文
def generate_enemy_hand():
    while True:
        yield "1"
        yield "2"
        yield "3"

## 出す手の配列
hand_dict = { 
    "1":"グー",
    "2":"チョキ",
    "3":"パー" 
}

## あいこ以外の処理
def is_win(my_hand,enemy_hand):
    if my_hand == "1" and enemy_hand == "2":
        return True
    elif my_hand == "2" and enemy_hand == "3":
        return True
    elif my_hand == "3" and enemy_hand == "1":
        return True
    return False

## ランダム値を出す標準ライブラリ
from random import randint

lose_count = 0
enemy_hands = generate_enemy_hand()


while True:
    
    my_hand = input("じゃんけん... 1:グー, 2:チョキ, 3:パー")
    

    if my_hand not in ("1", "2","3"):
        print("間違った入力です")
        continue
    enemy_hand = str(randint(1,3))
    print("あなたの出した手は : {}, 相手の出した手は : {}".format(hand_dict.get(my_hand),hand_dict.get(enemy_hand)))


    if my_hand == enemy_hand:
        print("あいこ")
    elif is_win(my_hand, enemy_hand):
        print("あなたの勝ちです")
        break
    else:
        lose_count += 1
        if lose_count == 3:
            print("あなたの負けです")
            break
        else:
            print("あなたの負けです。もう一回!")