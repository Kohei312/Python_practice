## Private変数 : 外部からアクセスできない変数のこと(pythonでは厳密に設定はできない。。。)
## 書き方 : __変数

class Human:
    __class_val = "Human"

    def __init__(self,name,age):
        self.__name = name # プライベート変数
        self.age = age
    def print_msg(self):
        print("name = {}".format(self.__name)) # クラス内では参照可能

human = Human("Taro", 15)
# print(human.name) # アクセスエラー
# print(human._Human__name) # インスタンスからアクセスできなくはない（実務ではほとんど使わない）

human.print_msg() # name = Taro