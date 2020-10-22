## 線形探索 : 冒頭から順番に探す方法

ex_list = [1,2,3,34,5,6,7,8,9,9,10]

found = False

for i in range(len(ex_list)):
    if ex_list[i] == 34:

        print("found : {}".format(i))
        found = True
        break ## ループ終了
    else:
        print("not found")

