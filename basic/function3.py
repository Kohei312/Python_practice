## グローバル変数

## グローバル変数を使わない場合
# animal = "dog"

# def printAnimal():
#     animal = "cat"
#     ## ここで関数外bのanimalが更新されるわけではない →参照している変数のメモリアドレスが異なるから
#     print("関数内animal = {}, id = {}" .format(animal,id(animal))) # 関数内animal = cat, id = 4320711408


# printAnimal()
# print("関数外animal = {}, id = {}" .format(animal,id(animal))) # 関数外animal = dog, id = 4320711152


## グローバル変数を使った場合
# animal = "dog"

# def printAnimal():
#     ## "cat"を代入する引数を、関数外にあるanimalと同じものを参照していることを宣言
#     ## →グローバル化しているため、関数内に記述していても、関数外から直接呼び出すこともできる
#     global animal
#     animal = "cat"
#     print("関数内animal = {}, id = {}" .format(animal,id(animal))) # 関数内animal = cat, id = 4518876080


# printAnimal()
# print("関数外animal = {}, id = {}" .format(animal,id(animal))) # 関数外animal = cat, id = 4518876080
