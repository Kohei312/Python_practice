## 関数

## 書き方
# def 関数名():
#     処理

def print_hello():
    print("Hello World")

print_hello()

## 引数の型を記入しても、強制力はない...
def num_max(a: int, b: int):
    print("a = {}, b = {}".format(a,b))
    if a > b:
        return a
    else:
        return b

print(num_max(10,20))