## デコレータ関数

def my_decorator(func):
    # 内部関数
    def wrapper(*arg,**kwarg):
        print('*' *100)
        func(*arg, **kwarg)
        print('*' *100) 
    return wrapper

@my_decorator
def func_a(*arg, **kwarg):
    print("func_aを実行")
    print(arg)


@my_decorator
def func_b(*arg, **kwarg):
    print("func_bを実行")
    print(arg)

func_a(1,2,3)
func_b(1,2,3)