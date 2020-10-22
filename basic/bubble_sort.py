## バブルソート

list_a = [1,5,9,6,7,4,2,3,8]

# for i in range(len(list_a)):

#     ## j : 0からスタート => (list_aの長さ -1) -i -1
#     ## → 1回のソートで配列の何番目まで移動するか
#     ## 1回目 : len(list_a) = 8, i = 0, => 7
#     ## 2回目 : len(list_a) = 8, i = 1, => 6
#     ## 3回目 : len(list_a) = 8, i = 2, => 5
#     ## 4回目 : len(list_a) = 8, i = 3, => 4
#     ## 5回目 : len(list_a) = 8, i = 4, => 3
#     ## 6回目 : len(list_a) = 8, i = 5, => 2
#     ## 7回目 : len(list_a) = 8, i = 6, => 1
#     ## 8回目 : len(list_a) = 8, i = 7, => 0 
#     ## →だんだんソートする範囲が狭まっていく
#     for j in range(0, len(list_a) - i -1):

#         ## jよりも右側にある値のほうが、jの値よりも大きいかどうか比較
#         if list_a[j] < list_a[j+1]:
#             ## 大きい場合は入れ替え
#             list_a[j], list_a[j+1] = list_a[j+1], list_a[j]

# print(list_a)

def bubble_sort(s):

    for i in range(len(s) - 1): ##  0 から range(len(s) - 1)までの範囲を検索

        # i の回数分 * indexの数だけ、以下がループする
        # ex) i = 0のとき、list[0]の値を対象に処理を開始する
        for index in range(0, (len(s) -1) - i): ## 計算範囲を、(len(s) - 1) - (計算対象数・計算済み数を除いた数) に絞り込む
         # ex) 0 から (8 -0) = 8 の範囲で、以下の処理を繰り返し行う
            print("i :{}, index:{}".format(i,index))
            if s[index] < s[index + 1]: ## ここで比較. この場合は、昇順
                s[index], s[index + 1] = s[index +1], s[index]
                print("s = {}".format(s))

print(bubble_sort(list_a))