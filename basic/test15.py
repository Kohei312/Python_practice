## if文
## 偽とされる値は、None,false,0,'',{},{:},(),[]

# num = {"":""}

# print('計算結果: {}'.format(bool(num)))
# if num:
#     print("処理開始")


class hoge():

    def __init__(self,a):
        self.a = a
    
    def __bool__(self):
        if self.a == 'a':
            return True
        return False

st_hoge = hoge('b')

print('計算結果: {}'.format(bool(st_hoge)))
if st_hoge:
    print("処理開始")
