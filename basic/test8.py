## 文字列

# fruit = "apple"
## 文字列型の変数に格納された値を、コピーすることも可能
## 以下で,fruitに"apple"が10コ代入される
# fruit * 3
## 以下の書き方と同様
# fruit = """apple
# apple
# apple
# """

## 以下で、fruit内の文字列のうち、10番目の文字を取得可能
# print((fruit)[10])
## 以下では、fruit変数に格納された"apple"のうち、aから-1番目の文字を取得する
# print((fruit)[-1])

## 文字列メソッド : 変数名(オブジェクト名).メソッド名()

## byte型（データ型）への変換：encode,decode
### encode
# byte_fruit = fruit.encode('utf-8')
# print(byte_fruit) # b'格納された値' で表現される
# print(type(byte_fruit))

### decode
# str_fruit = byte_fruit.decode('utf-8')
# print(str_fruit)
# print(type(str_fruit))
## count：文字列内に、指定された文字がいくつあるかを返す
### 引数：（element,start,end）→ elementでカウントする要素を指定する。start,endは検索する範囲を指定（オプション）
# msg = 'abcdefabc'
# print(msg.count('a'))


## 文字列の 始まり/終わり をチェック：startswith, endswith
### 指定した文字列から始まる / 文字列で終わるか　を判別する。返り値はbool型
### startwithは割と実務で使う
# print(msg.startswith('abcd')) # => True
# print(msg.startswith('fff')) # => false
# print(msg.endswith('abc')) # => True
# print(msg.endswith('abcd')) # => False

# 文字列の削除 : strip(両端のスペース・文字を削除), rstrip（右端を削除）, lstrip（左端を削除）
## 文字列内の順番に関係なく削除可能
# msg = 'abcdefabc'
# print(msg.strip('cba'))
# print(msg.rstrip('cba'))
# print(msg.lstrip('cba'))

## 文字列の変換 : upper,lower, swapcase, replace, capitalize
# msg = 'abcABCabc'
# msg_u = msg.upper() ## すべて大文字
# print(msg_u) # ABCABCABC
# msg_l = msg.lower() ## すべて小文字
# print(msg_l) # abcabcabc

# msg_s = msg.swapcase() ## 大文字 ⇆　小文字
# print(msg_s) ABCabcABC

## replace
### replaceの引数: ('置換元の値', '置換後の値', Int(0からどこまでの範囲で置換するか)) 
# msg_r = msg.replace('abc','FFF',2)

# print(msg_r) # FFFABCabc

## capitalize
### 文字列内の先頭の文字だけを大文字、その他を小文字に変換する
# msg = "hello WoRld"
# print(msg.capitalize()) # Hello world

## 文字列型の取り出し ：　format, islower, isapper

# ## 以下で、:以前の文字列を取得する
# print(msg[:5]) # hello

# ## 以下で、:以降の文字列を取得する
# print(msg[6:]) # myname is TARO

# ## 以下で、取得する文字列の範囲を指定できる
# print(msg[1:6]) # ello,

# ## 以下で、2つ目の:後の値ごとに飛ばして、取得する文字列の範囲を指定できる
# ## 以下の例では、"hello,my name is TARO"のうち、1番目の文字を起点に、2つごとに飛ばして値を取得している
# print(msg[1:6:2]) # el,  


## format
# msg = 'hello,my name is TARO'
# print('英語でのあいさつは, {}'.format(msg))
# name = 'JIRO'
# print(f'hello {name}') # 3.6以上
# print(f'{name =}') # 3.8以上


## islower : 文字列がすべて小文字かどうか判定。返り値はbool型
# msg = 'apple'
# print(msg.islower()) # TRUE

## isupper : 文字列がすべて大文字かどうか判定。返り値はbool型
# msg = 'ORANGE'
# print(msg.isupper()) # TRUE

## find, index, rfind, rindex
## find : 指定した文字列が、左から何番目にあるのか検索。返り値はInt型。ヒットした文字列の最初にある文字の位置が,返り値となる。
## 値が見つからない場合は -1
msg = 'ABCDEABC'
print(msg.find('DE')) # 3
print(msg.find('F')) # -1

## rfind : 右側から検索して、指定した文字列が何番目にあるか検索。
## 値が見つからない場合は -1
print(msg.rfind('ABC')) # 5
print(msg.find('F')) # -1

## index : 指定した文字列が、左から何番目にあるのか検索。返り値はInt型。ヒットした文字列の最初にある文字の位置が,返り値となる。
## 値が見つからない場合は エラー
print(msg.index('DE')) # 3
print(msg.index('F')) # Traceback (most recent call last) : ・・・  

## rindex : 右側から検索して、指定した文字列が何番目にあるか検索。
## 値が見つからない場合は エラー
print(msg.rindex('ABC')) # 5
print(msg.index('F')) # Traceback (most recent call last) : ・・・  