## 幅優先探索 : 近いところからリストアップし、それぞれ同じ層で細かく調べる方法

tree = [ [1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14],[],[],[],[],[],[],[],[],[] ]

data = [0]
while len(data) > 0:
    pos = data.pop(0) # dataから値を取り出す. 0
    # print(pos,end=' ')

    for i in tree[pos]:
        data.append(i)
        print("data : {}".format(data))

# data : [1]
# data : [1, 2]
# data : [2, 3]
# data : [2, 3, 4]
# data : [3, 4, 5]
# data : [3, 4, 5, 6]
# data : [4, 5, 6, 7]
# data : [4, 5, 6, 7, 8]
# data : [5, 6, 7, 8, 9]
# data : [5, 6, 7, 8, 9, 10]
# data : [6, 7, 8, 9, 10, 11]
# data : [6, 7, 8, 9, 10, 11, 12]
# data : [7, 8, 9, 10, 11, 12, 13]
# data : [7, 8, 9, 10, 11, 12, 13, 14]