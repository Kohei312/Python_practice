## 例外処理(try, except)

## try: 
##   実行したい処理
## except (エラー名):
##   例外発生時の処理

try:
    # a = 10 / 0
    b = ["10","20","30"]
    # c = b[4]
    # d = hoge()
except ZeroDivisionError as e:
    ## エラーの詳細を表示したいとき : tracebackという標準ライブラリを使用して表示
    import traceback
    traceback.print_exc()

    # print(e,type(e))
    pass # 結果にかかわらず、処理を進める記述
except IndexError as e:
    print("indexError : {}".format(e))
except Exception as e:
    print("Exception :",e,type(e))
else:
    # a = 10 / 0  # エラーキャッチできない
    print("else処理")
finally:
    print("finally処理")
print("処理完了")

## exceptのエラーについて
### FileNotFoundError : プログラムで指定されたファイルが見つからないエラー
### IndexError : 配列などで指定したインデックスに値が存在しないエラー
### TypeError : 型に関するエラー
### ZeroDivisionError : 0で割ろうとしたことによるエラー
### Exception : すべての例外

## else, finally
### else : 例外が発生しなかった場合に実行される.例外発生時は実行されない. else内で発生したエラーはcatchできないため注意
### finally : 例外が発生しなかった場合も、発生した場合も実行される.

## raise : 例外を呼び出し元に返す処理

class MyException(Exception): # 引数内に継承するクラス型を指定
    pass

def devide(a,b):
    if(b == 0):
        # raise ZeroDivisionError("bを0に設定しない")
        raise MyException("bを0に設定しない")
    else:
        return a/b

try:
    result = devide(10,0)
except Exception as e:
    print("{} : {}".format(type(e),e)) # <class '__main__.MyException'> : bを0に設定しない
