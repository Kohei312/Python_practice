# 高階関数

# def print_hello():
#     print("hello") 

# def print_goodbye():
#     print("goodbye")

# var = ["aa","bb", print_hello,print_goodbye]
# # var[1]() # エラー

# var[2]() # インスタンス化してdef起動. hello
# var[3]() # goodbye

def print_world(msg):
    print("{} world".format(msg))

def print_konnichiwa():
    print("こんにちわ")

def print_hello(func):
    func("hello")
    return print_konnichiwa

var = print_hello(print_world) #print_helloを実行 => print_konnichiwa()が、代入される # hello world
var() #前文でprint_konnichiwa()が格納されているため、var()でprint_konnichiwaが実行される # こんにちわ