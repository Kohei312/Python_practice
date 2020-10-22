## リスト(配列)型


# list_a = [1,2,3,4]
# print(list_a[1]) # 2

## 異なる型のものも、混ぜ込んで使用できる
# list_a = [1,2,"apple",4]
# print(list_a[2]) # "apple"

## 指定する番号を -1のようにすると、後ろから値を取得する。このとき、配列の一番はじめにある値が[0]となり、基準となることは共通
# list_a = [1,2,"apple",4]
# print(list_a[-1]) # 4

## 多重配列も可能
# list_a = [10,20,[1,2,"apple",4],30]
# print(list_a[2]) # [1, 2, 'apple', 4]
# print(list_a[2][2]) # "apple"

# list_a[2][2] = "GRAPE"
# print(list_a[2][2]) # "GRAPE"

### リストのメソッド

## スライス : [検索を始める順番:検索を終える順番(ここは検索対象に含まれない!)], 検索を始める順番 =< 範囲 < 検索を終える順番　と同義
list_a = [10,20,[1,2,"apple",4],30]
# print(list_a[0:2]) # [10, 20]
## [1:10:n]とすると、 値を n 個とばしで取得する
# print(list_a[0:3:2]) # [10, [1, 2, 'apple', 4]]

## extend : 別のリストの要素を追加して拡張
# list_a.extend(['banana','grape'])
# print(list_a)  # [10, 20, [1, 2, 'apple', 4], 30, 'banana', 'grape']

## insert : 位置を指定して挿入する。挿入位置に指定された配列内の値は、ひとつ後ろに移動する。引数は、（挿入位置,挿入する要素）。
# list_a.insert(1,'hoge')
# print(list_a) # [10, 'hoge', 20, [1, 2, 'apple', 4], 30]

## clear : リスト内の値を全消去して、空の配列にする。
# list_a.clear()
# print(list_a) # []

## remove : 指定した値を削除する。削除する位置番号ではなく、要素を指定する点に注意!!
## 同じ値の要素が複数ある場合は、一番左にある値のみ消去する
# list_a.remove(20)
# print(list_a) # [10, [1, 2, 'apple', 4], 30]

## pop : 指定した位置の値を取り出して削除.引数を指定しなければ、デフォルトで末尾の要素が削除される。
## popした要素は、そのまま別の変数に代入することが可能。取り出すイメージ
# value = list_a.pop() # 30
# value2 = list_a.pop(2) # [1, 2, 'apple', 4]
# print(list_a, value) # [10, 20, [1, 2, 'apple', 4]], 30
# print(list_a, value2) # [10, 20, 30], [1, 2, 'apple', 4]

## count : 指定した値がいくつあるか数える。対象値と一致するものをピックアップする点に注意
## 対象値がない場合は、0が返ってくる。
# print(list_a.count(10)) # 1
# print(list_a.count("hoge")) # 0

## index : 指定した値がどこにあるか調べる。対象値と一致するものをピックアップする点に注意
## 対象値が見つからない場合はエラーとなる。値が複数存在する場合は、一番左にあるものがピックアップされる
# print(list_a.index(10)) # 0
# print(list_a.index(1)) # エラー

## copy : リストを複製する（値渡しの状態）
## 前提：変数を、別の変数に代入するのは「参照渡し（最初の変数のメモリを共有している状態）」
# print(list_a) # [10, 20, [1, 2, 'apple', 4], 30]
# list_b = list_a
# list_b[0] = "hoge"
# print(list_a) # ['hoge', 20, [1, 2, 'apple', 4], 30] ← list_aのメモリアドレスを参照して表示しており、参照先のlist_bで値が書き換えられると、参照元のlist_aの値も変わる

## copy()を使用すると、値は同じだがメモリアドレスは独立した変数が作られる。
## →copyされた配列内の値を書き換えても、copy元の値は変わらない.
## ただし、多重配列の場合はこのかぎりではないため、標準メソッドのcopyではなく、copyライブラリのdeepcopyというメソッドを使用するらしい（省略）
# print(list_a) # [10, 20, [1, 2, 'apple', 4], 30]
# list_b = list_a.copy()
# list_b[0] = "hoge"
# print(list_a) # [10, 20, [1, 2, 'apple', 4], 30]
# print(list_b) # ['hoge', 20, [1, 2, 'apple', 4], 30]


### 並べ替え
## sort, sorted :　同じ型のデータの時のみ使用可能。小さい値から大きい値へ順番に並び替えられる。
list_fruit = ['banana','apple','lemon','grape']
# print(list_fruit) # ['banana', 'apple', 'lemon', 'grape']
list_mix = ['あ','い','う','grape']
list_intstr = ['grape', 'う', 'い', 11]

## どちらも同じ操作
# list_fruit.sort() 
# list_fruit = sorted(list_fruit) 

# list_mix.sort()
# list_mix = sorted(list_mix)

# list_intstr.sort()
# list_intstr = sorted(list_intstr)

## sort,sortedの結果
# print(list_fruit) # ['apple', 'banana', 'grape', 'lemon']
# print(list_mix.sort()) # エラー（String型の場合、対象値の言語も統一されてる必要があるっぽい）
# print(list_intstr.sort()) # エラー

## reverse : 同じ型のデータの時のみ使用可能。リスト内の順番を逆転して入れ替える。昇順・降順に整理して並び変わるわけではない点に注意
list_fruit.reverse()
# list_mix.reverse()
# list_intstr.reverse()

print(list_fruit) # ['grape', 'lemon', 'apple', 'banana']
# print(list_mix.reverse()) # None（実質エラー.String型の場合、対象値の言語も統一されてる必要があるっぽい）
# print(list_intstr.reverse()) # None
