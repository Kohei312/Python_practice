## with詳細
## with クラス as a:
## 使い所: 処理が連続していて、すべての処理が必要な場合(トランザクション処理が必要な時)
### ex) ファイルへの書き込み処理（ファイル開く→書き込み→閉じる）
### ex) DBへのデータの書き込み処理（DBへコネクションを張る→書き込む→コネクションを閉じる）

# class WithTest:

#     def __init__(self): 
#         print("init called") # 1番目に呼ばれる
    
#     def __enter__(self): 
#         print("enter called") # 2番目に呼ばれる

#     def __exit__(self, exc_type,exc_val, traceback): 
#         print("exit called") # 4番目に呼ばれる

# with WithTest() as f: # ここで処理開始
#     print("with の中") # 3番目に呼ばれる

# class WithTest:

#     def __init__(self,msg): 
#         print("init called") # 1番目に呼ばれる
#         self.msg = msg
    
#     def __enter__(self): 
#         print("enter called") # 2番目に呼ばれる
#         print(self.msg) # 3番目に呼ばれる

#     def __exit__(self, exc_type, exc_val, traceback):  # 第2~4引数は、エラーハンドリングに用いられる
#         print("exit called") # 5番目に呼ばれる

# with WithTest("Hello") as f: # ここで処理開始
#     print("with の中") # 4番目に呼ばれる

class WithTest:

    def __init__(self,file_name): 
        print("init called") # 1番目に呼ばれる
        self.__file_name = file_name
    
    def __enter__(self): 
        print("enter called") # 2番目に呼ばれる
        self.__file = open(self.__file_name,mode="w",encoding="utf-8")
        return self # 変数 f へ格納される

    def write(self, msg):
        self.__file.write(msg)

    def __exit__(self, exc_type, exc_val, traceback):  # 第2~4引数は、エラーハンドリングに用いられる
        print("exit called") # 5番目に呼ばれる
        self.__file.close()

with WithTest("basic/resources/output.txt") as f: # ここで処理開始
    print("with の中") # 4番目に呼ばれる
    f.write("ああああああああい")