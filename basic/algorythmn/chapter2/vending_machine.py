## 数字だけでなく、実際の硬貨・紙幣を返す処理を組む

import sys # エラー時に強制終了するためのモジュール

insert_prince = input("いくら支払いますか？") # 投入金額
if not insert_prince.isdecimal():
    print("整数を入力してください")
    sys.exit()

product_price = input("商品金額はいくらですか？") # 商品金額
if not insert_prince.isdecimal():
    print("整数を入力してください")
    sys.exit()

change =  int(insert_prince) - int (product_price)

money_list = [5000,1000,500,100,50,10,5,1]

if change < 0:
    print("支払金額が、あと {} 円 たりません".format(- change))
    sys.exit()
else:
    for money in money_list:
        r = change // money
        change %= money # change = change % moneyのこと
        print("{} 円： {} 枚".format(money,r))


    # r5000 = change // 5000 ## ここで5000円札の枚数を指定。 //で割り算、商が枚数。
    # q5000 = change % 5000 ## あまりが残額
    # print("5,000円札 : {} 枚".format(r5000))        

    # r1000 = q5000 // 1000 ## ここで5000円札の枚数を指定。 //で割り算、商が枚数。
    # q1000 = q5000 % 1000 ## あまりが残額
    # print("1,000円札 : {} 枚".format(r5000))

    # r500 = q1000 // 500 ## ここで5000円札の枚数を指定。 //で割り算、商が枚数。
    # q500 = q1000 % 500 ## あまりが残額
    # print("500円玉 : {} 枚".format(r5000))

    # r100 = q500 // 100 ## ここで5000円札の枚数を指定。 //で割り算、商が枚数。
    # q100 = q500 % 100 ## あまりが残額
    # print("100円玉 : {} 枚".format(r5000))

    # r50 = q100 // 50 ## ここで5000円札の枚数を指定。 //で割り算、商が枚数。
    # q50 = q100 % 50 ## あまりが残額
    # print("50円玉 : {} 枚".format(r5000))

    # r10 = q50 // 10 ## ここで5000円札の枚数を指定。 //で割り算、商が枚数。
    # q10 = q50 % 10 ## あまりが残額
    # print("10円玉 : {} 枚".format(r5000))

    # r5 = q10 // 5 ## ここで5000円札の枚数を指定。 //で割り算、商が枚数。
    # q5 = q10 % 5 ## あまりが残額
    # print("5円玉 : {} 枚".format(r5000))

    # r1 = q5 // 1 ## ここで5000円札の枚数を指定。 //で割り算、商が枚数。
    # # q100 = q500 % 100 ## あまりが残額 ここは0になるはず
    # print("1円玉 : {} 枚".format(r5000))