## インスタンスメソッド : クラスから作成したオブジェクト(インスタンス)を用いて呼び出すメソッド
### 作成方法: クラス内に。defでメソッドを作成する。
### 注意点： メソッドの第1引数にはselfを使用する。 ←クラス自身を実体化し、オブジェクトを実行可能な状態にするため
### 呼び出し方 : クラス名.メソッド名()

class MyClass:
    def __init__(self,name):
        self.name = name
    def print_hello(self):
        print("Hello" + self.name)

# AClass = MyClass("World")
# AClass..print_hello()




## クラスメソッド :  クラスをインスタンス化せずに実行できるメソッド
class YourClass:
    class_name = "YourClass"
    def __init__(self,name):
        self.name = name   # インスタンスの初期化前にクラスメソッドが呼ばれるため、インスタンス変数へのアクセスは不可。そもそもない。
    @classmethod # 対象のメソッドの直上に、@classmethodをつける
    def print_hello(cls): # 第１引数に、clsを取る
        print("Hello" + cls.class_name)  # クラス内の値を参照する場合は、clsのオブジェクトとして取得する

# AClass = MyClass("World") # クラスの初期化が必要ない
# デメリット : クラス内にある変数に直接アクセスすることはできない（__init__内）
# YourClass.print_hello()

## スタティックメソッド : インスタンスメソッドやクラスメソッドのように、
## インスタンスやクラスが引数に渡されることはしない。
### インスタンスメソッドとの使い分け...??

class OtherClass:

    def __init__(self,name):
        self.name = name   # インスタンスを初期化するため、インスタンス変数にアクセス可能
    @staticmethod # 対象のメソッドの直上に、@staticmethodをつける
    def print_hello(name): # 第１引数をとらない
        print("Hello" + name) 

## 以下の2パターン
hoge = OtherClass("hoge")
print(hoge.name) ## インスタンス化しているため、インスタンス変数にアクセス可能
hoge.print_hello("huga")

## 別パターン
OtherClass.print_hello("hoge")