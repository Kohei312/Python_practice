## ポリモーフィズム

from abc import abstractmethod,ABCMeta

class Human(metaclass=ABCMeta): #親クラス

    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def say_something(self):
        pass

    def say_name(self):
        print(self.name)

class Woman(Human):
    
    def say_something(self): # ここでオーバーライドする必要がある
        print("ごきげんうるわしゅう, {}".format(self.name))
# human = Woman("hanako")    

class Man(Human):
    
    def say_something(self): # ここでオーバーライドする必要がある
        print("やあ, {}".format(self.name))
    
num = input("0または1を入力してください")
if num == "0":
    human = Man("Taro")
elif num == "1":
    human = Woman("Hanako")
else:
    print("エラー")

# 上記の条件分岐で、humanが共通の親クラス（Human）を継承しているが、どちらの子クラスを実際に継承するのかを決めて実行される
# どっちのクラスになっても、共通メソッドsay_something()は実行可能
human.say_something() 