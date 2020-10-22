## 特殊メソッド
## インスタンスへアクセス時に、特定の処理を実行すると呼び出されるメソッド。


class Human:
    def __init__(self, name,age,phone):
        self.name = name
        self.age = age
        self.phone = phone

    def __str__(self):
        return self.name + "," + str(self.age) + "," + str(self.phone)

    def __eq__(self, other):
        return (self.name == other.name) and (self.phone == other.phone)

    def __hash__(self):
        return hash(self.name + self.phone)

    def __bool__(self):
        return True if self.age >= 20 else False
    
    def __len__(self):
        return len(self.name)
            


man = Human("Taro",20,"080109203910")
man_str = str(man)
# print(man_str) # __str__が内部で自動で呼び出される. Taro, 20, 080109203910


man2 = Human("Jiro",10,"080109203910") 
# print(man == man2)  # __eq__が内部で自動で呼び出される. False


# print(hash("Taro")) # 同じ値を渡すと、同一のハッシュ値が渡される => 重複を避けることができる
# print(hash("Taro"))
# print(hash("Jiro"))

man3 = Human("ki",20,"080109203910") 
set_men = {man,man2,man3}
# for x in set_men:
#     print(x) # Jiro,20,080109203910, Taro,20,080109203910

# if man: ## __bool__を内部で自動で呼ぶ
#     print("manはTrue") # True
# if man2:
#     print("man2はTrue") # False

print(len(man)) ## __len__を内部で自動で呼ぶ. 4
print(len(man3)) ## 2
