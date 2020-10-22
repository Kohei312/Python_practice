## セット型 ( { "値1", "値2"  }で書く )
## →同じ値を持てない（一意の値（ハッシュ値）のみ持てる）、順序が保持されていない。集合処理（ユニオン、インターセクションなど）を高速処理できる

set_a = {"a","b","c","d","a",12}
# print(set_a) # {'b', 'c', 'd', 12, 'a'} ←　順序は出力のたびに変わる

## 以下の例では、辞書型で一意性を保てないため、エラーとなる。
# set_b = {"a","b","c","d","a",12,["a","b"]}
# print(set_b) # エラー ←

## セット内に、特定の値が含まれているかチェックする
# print("e" in set_a) # False
# print("a" in set_a) # True

# print("e" not in set_a) # True
# print("a" not in set_a) # False

## len : セットの長さを返したい場合
# print(len(set_a))

## add : セットに値を追加する
# set_a.add("M")
# print(set_a) # {'d', 12, 'a', 'M', 'c', 'b'}

## remove : セットから値を削除する. 要素が存在しない場合は、エラーとなる
# set_a.remove("a")
# print(set_a) # {'d', 'b', 12, 'c'}

# set_a.remove("BB")
# print(set_a) # エラー


## discard : セットから値を削除する. 要素が存在しない場合は、なにも処理せず、そのままのセット値が返ってくる
# set_a.discard(12)
# print(set_a) # {'b', 'a', 'd', 'c'}

# set_a.discard(100)
# print(set_a) # {'a','d', 'b', 12, 'c'}

## pop : 1つの値をランダムに取り出す
# val = set_a.pop()
# print(val, set_a)　# 12 {'d', 'c', 'a', 'b'} ←　取り出す値は毎回変わる

## clear : セット内の値を空にする
# set_a.clear()
# print(set_a) # set()
  
