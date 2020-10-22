## inner関数, ノンローカル変数

## inner関数の用途
### 1. 関数外からアクセスできないようにする
### 2. 関数の中での繰り返し処理を、1つにまとめる
### 3. デコレータ関数を作成する

# def outer():
#     ## outer関数内で、inner関数を作成・呼び出しまで行う
#     def inner():
#         print("A")
#     inner()

# ## inner関数を呼び出すときは、outer関数を呼び出して間接的に呼び出す。
# outer()
# # inner() # これだとエラーになる


## ノンローカル変数
## outer関数内で定義された変数と、inner関数内で宣言された変数は別物として認識される. globalと宣言しても意味なし
## →この場合、inner関数内で nonlocal を宣言することで、outer関数で宣言した変数をグローバル変数っぽく扱えるようになる（outer関数内のみ）
def outer2():
    # nonlocal outer_value # ここに記述するとエラー
    outer_value = "外側の変数"
    def inner():
        nonlocal outer_value #ここに記述する
        outer_value = "内側の変数"
        print("inner : outer_value = {}, id={}".format(outer_value,id(outer_value))) # inner : outer_value = 内側の変数, id=4413323088  
    inner()
    print("outer : outer_value = {}, id={}".format(outer_value,id(outer_value))) # outer : outer_value = 外側の変数, id=4413322992

outer2()
# print(outer_value) # これはエラーとなる