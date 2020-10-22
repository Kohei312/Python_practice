
### セット型 メソッド 
## union : 和集合. それぞれの要素が重なった集合部分を除いた集合を返す. |　で表す
## intersection :  積集合. 共通した集合のみを返す. & で表す
## difference : 差集合. 片方の集合にあり、片方の集合にない要素を返す. - で表す
## symmetric_difference : どちらか一方にだけある要素の集合を返す. ^ で表す

s = {'a','b','c','d'}
t = {'c','d','e','f'}

## union : 和集合. それぞれの要素が重なった集合部分を除いた集合を返す. |　で表す
# u = s | t
# # u = s.union(t) # これも同じ意味
# print(u)  # {'c', 'a', 'e', 'd', 'f', 'b'} ←順列は保証されない

## intersection :  積集合. 共通した集合のみを返す. & で表す
# u = s & t
# # u = s.intersection(t) # これも同じ意味
# print(u) # {'d', 'c'} ←順列は保証されない


## difference : 差集合. 片方の集合にあり、片方の集合にない要素を返す. - で表す
# u = s - t # sにあって、tにないものが返ってくる
# # u = s.difference(t) # これも同じ意味
# print(u) # {'b', 'a'} ←順列は保証されない

## symmetric_difference : どちらか一方にだけある要素の集合を返す. ^ で表す
# u = s ^ t # どちらか一方にしかない要素を返す。
# # u = s.symmetric_difference(t) # これも同じ意味
# print(u) # {'e', 'a', 'f', 'b'} ←順列は保証されない 

## |= : 要素の追加
# s |= t
# print(s) # {'e', 'd', 'f', 'c', 'a', 'b'}

## issubset, issuperset, isdisjoint
x = {'apple', 'banana'}
y = {'apple', 'banana','lemon'}
z = {'cherry'}

## 変数.issubset(引数) : 要素がすべて引数内のセット型の変数にあるかどうか
# print(x.issubset(y)) # True
# print(z.issubset(y)) # False

## 変数.isupserset(引数) : 引数内のセット型の変数が、メソッドを実行した変数内にすべてあるかどうか
# print(x.issuperset(y)) # False
# print(z.issuperset(y)) # False
# print(y.issuperset(x)) # True

## 変数.isdisjoint(引数) : 引数内のセット型の変数が、メソッドを実行した変数内に含まれていないかどうか
print(y.isdisjoint(x)) # False →含まれている
print(y.isdisjoint(z)) # True  →含まれていない
