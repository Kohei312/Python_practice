## カプセル化, getter, setter
## 使い方 その１
# class Human:

#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age

#     def get_name(self):
#         print("getter name を呼び出しました")
#         return self.__name

#     def get_age(self):
#         print("getter age を呼び出しました")
#         return self.__age

#     def set_name(self, name):
#         print("setter name を呼びました")
#         self.__name = name
   
#     def set_age(self, age):
#         print("setter age を呼びました")
#         self.__age = age

#     name = property(get_name, set_name) # nameを指定すると、get_name, set_nameが呼び出される
#     age = property(get_age,set_age)

#     def print_msg(self):
#         print(self.name,self.age)
    
# human = Human("Taro",20)
# human.name = "Jiro" # set_nameが実行される
# human.age = 39 # set_ageが実行される
# human.print_msg()

## 使い方 その２: getterでは @property, setterでは @hoge.setterと記載していく
class Human:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):  # これがgetterになる
        print("getter name を呼び出しました")
        return self.__name

    @property
    def age(self):
        print("getter age を呼び出しました")
        return self.__age

    @name.setter
    def name(self, name):
        print("setter name を呼びました")
        self.__name = name
    
    @age.setter
    def age(self, age):
        print("setter age を呼びました")
        if age < 0:
            print("0以上の値を入れてください")
            return
        self.__age = age

human = Human("Hoge",25)
human.name = "Huga"
human.age = -1
print(human.name)

    