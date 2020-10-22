## ファイル出力(今回は,resourcesディレクトリ/write.csv を利用)
## 引数は、(ファイル相対パス, mode="w( writeの意味 )", encoding="utf-8")で指定する
file_path = "basic/resources/write.csv"
# f = open(file_path, mode = "w", encoding="utf-8", newline='\n') ## ファイルが存在する場合→上書き処理(これまでのデータは消去される点に注意), 存在しない場合→作成処理が行われる

## 書き込み処理
# f.write("文字列")
### リストをそのままつなげて書き込み
# f.writelines()
### リストを改行しながら書き込み
# f.write("¥n".join(list))

# f.write("あああ\nいいい\nううう") # ここでファイル作成または上書き処理が実行
# f.close()

## これもwithで書くのがおすすめ
# with open(file_path,mode="w",encoding="utf-8",newline="\n") as f:
#     list_a =[ 
#         ["A","B","C"],
#         ["あ", "い", "う"]
#     ]
#     f.writelines(list_a[0])


## ファイルへの追記(今回は,resourcesディレクトリ/write.csv を利用)
## 引数は、(ファイル相対パス, mode="a", encoding="utf-8")で指定する
with open(file_path,mode="a",encoding="utf-8",newline="\n") as f:
    list_a =[ 
        ["D","E","F"],
        ["あ", "い", "う"]
    ]
    for x in list_a:
        f.write("\n")
        f.write(",".join(x))
    # f.writelines(list_a[1])


### バイナリファイルへの読み書き => modeに b をつける
# open(file_path, mode='rb') # バイナリファイルの読み込み
# open(file_path, mode='wb') # バイナリファイルへの書き込み