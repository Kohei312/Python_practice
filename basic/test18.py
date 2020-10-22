## ループ文(for, while)

## for 変数 in 範囲:
##    処理
## for文の範囲に、range関数を使用することがある

## 最終値は含まれない(< 最終値)範囲が対象となる点に注意
## 引数が 1つ : 範囲の最終値を指定する 
# for i in range(5):
#     print(i) # 0,1,2,3,4

## 引数が 2つ : 範囲の開始値、最終値を指定する 
# for i in range(2,6):
#     print(i) # 2,3,4,5

## 引数が 3つ : 範囲の開始値, 最終値, nコ飛ばしを指定する 
# for i in range(0,10,1):
#     print(i) # 0,3,6,9

## タプルでも実行可能
# sample = ("a","b","c")
# for sam in sample:
#     print(sam) # a, b, c

## 辞書型でも実行可能
# dic = {"キー1":"a","キー2":"b","キー3":"c",}
# for d in dic:
#     print(d,dic.get(d)) # キー1,a  キー2,b  キー3,c


## while (条件式) : (条件式)の結果がTrueになるまで処理を続ける
# count = 0
# while count < 10:
#     print(count)
#     count += 1