## コンストラクタ : インスタンス生成時に呼び出す

class SampleClass:

    def __init__(self, msg, name=None): # コンストラクタ
        print("コンストラクタ作成")
        self.msg = msg
        self.name = name

    ## デストラクタ : インスタンス削除時に自動的に呼び出される
    def __del__(self):
        print("デストラクタ実行")
        print("name = {}".format(self.name))

    def print_msg(self):
        print(self.msg)

    def print_name(self):
        print(self.name)

var_1 = SampleClass("hello","jiro") # コンストラクタ作成
var_1.print_msg() # hello
var_1.print_name() # jiro
del var_1

