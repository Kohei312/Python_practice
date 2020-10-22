## バトル処理

class AllCharactors:
    all_charactors = []
    alive_charactors = []
    dead_charactors = []

    @classmethod
    def charactor_append(cls, name):
        if name in cls.all_charactors:
            raise CharactorAlreadyExistException("すでに存在する名前です")
        cls.all_charactors.append(name)
        cls.alive_charactors.append(name)

    @classmethod
    def charactor_delete(cls, name):
        cls.alive_charactors.remove(name)
        cls.dead_charactors.append(name)    

class CharactorAlreadyExistException(Exception):
    pass


class Charactor:
    
    def __init__(self,name,hp,offence,defense):
        AllCharactors.charactor_append(name)
        self.name = name
        self.hp = hp
        self.offence = offence
        self.defense = defense
    
    def attack(self, enemy, critical_point=1):
        if self.hp <= 0:
            print("勝敗はつきました")
            return
        attack_point = self.offence - enemy.defense
        attack_point = 1 if attack_point <= 0 else attack_point
        enemy.hp -= attack_point * critical_point

        if enemy.hp <= 0:
            AllCharactors.charactor_delete(enemy.name)            
        
    
    def critical_attack(self,enemy):
        self.attack(enemy, 2)

charactor_a = Charactor("A",10,5,3)
charactor_b = Charactor("B",8,6,2)

# print(charactor_b.hp)
# charactor_a.critical_attack(charactor_b)
# print(charactor_b.hp)


# print(AllCharactors.all_charactors)
# print(AllCharactors.alive_charactors)
# print(AllCharactors.dead_charactors)

# charactor_a.attack(charactor_b)
# print(charactor_b.hp)

# print(AllCharactors.all_charactors)
# print(AllCharactors.alive_charactors)
# print(AllCharactors.dead_charactors)

# charactor_b.attack(charactor_a)

charactor_c = Charactor("A",10,5,3)