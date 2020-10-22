## 2分探索

# def binary_search(arr, target): # 第1引数:昇順にソートされた配列, 第2引数 : 探索したい値
#     left = 0 # 探索の左端
#     right = len(arr) -1 #探索の右端
#     for _ in range(len(arr)):
#         search_idx = (left + right) // 2 # 中間値（探索のインデックス）
#         if arr[search_idx] == target:
#             return search_idx
#         elif arr[search_idx] > target: # 探索値より大きかった場合
#             right = search_idx - 1
#         elif arr[search_idx] < target: # 探索値より小さかった場合
#             left = search_idx + 1
#         if left > right:
#             return -1

# a = [1,2,3,4,5,6,8]
# print(binary_search(a, 7))



## 2分探索では、バイナリーサーチツリーでデータを作成する必要がある。
## →前提条件 : あるノードの値Xに対し、左に含まれるノードの値はXより小さく、右の含まれるノードの値はXより大きくする
## →対象数と、リスト内の数値を比較し、大きいグループ・小さいグループに2分するため、リストは昇順または降順にソートされている必要がある
a_list = [1,2,3,4,5,6,7,8]

## 2分探索フロー：
## 検索する間隔を半分に分割しながらデータを探す。

## 中央値を求める

# s = a_listとする
def search(s, num):

    ## 下限と上限インデックスを設定する
    left = 0
    right = len(a_list)-1

    while len(a_list)-1: ## 必ずリスト内にあるはずなので、リストの長さ -1 だけ繰り返し検索処理を行う

        center_index = (left + right) // 2 # => 下限 + 上限を2分して、中央インデックスを抽出
        print("left : {}, right : {}".format(left,right))
        print(center_index)

        center = s[center_index] # 中央インデックスから、中央値を抽出
        if num == center:
            print("終了. center :{}".format(center_index))
            break
        elif num < center:
            print("小さいグループで検索続行")
            right = center_index -1 ## 上限インデックスを更新
        elif num > center:
            print("大きいグループで検索続行")
            left = center_index +1 ## 下限インデックスを更新


print(search(a_list, 3))