## クラスの継承

class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    
    def greeting(self):
        print("hello {}".format(self.name))
    
    def say_age(self):
        print("{} 才です".format(self.age))

class Employee(Person): ## Personを継承

    def __init__(self, name, age, number):
        super().__init__(name,age)
        self.number = number

    def say_number(self):
        print("nuberは {}".format(self.number))

    def greeting(self): # オーバーライド : 処理内容を上書きすること
        super().greeting()
        print("従業員です. numberは{}".format(self.number))
    
    # def greeting(self, age): # オーバーロード : 引数を更新する（pythonではオーバーロードできない。。。）


man = Employee("hoge", 20, "0802981920291") 
man.greeting()
man.say_age()
man.say_number()