## ファイル使用(今回は,resourcesディレクトリ/input.csv を利用)
## 引数は、(ファイル相対パス, mode="r( readの意味 )", encoding="utf-8")で指定する
file_path = "basic/resources/input.csv"
f = open(file_path, mode = "r", encoding="utf-8")

# line = f.read()  
# print(line) # 1,2,3 a,b,c A,B,C あ,い,う ←文字列を取得

# lines = f.readlines() 
# print(lines) # ['1,2,3\n', 'a,b,c\n', 'A,B,C\n', 'あ,い,う'] ←行間区切りのある配列型で取り出せる

# for x in lines:
#     print(x.rstrip("\n")) # 1,2,3 a,b,c A,B,C あ,い,う ←文字列を取得


## readline : 1行ずつ読み込む
# line = f.readline()
# while line:
#     print(line.rstrip('\n'))
#     line = f.readline()
# ↓のように、セイウチ演算子で書き換え可能
while (line := f.readline()):
    print(line.rstrip('\n'))

f.close() #ファイルを閉じる **お約束

## ファイルを開いているデメリット : メモリを消費する。ほかの処理でファイルを開けなくなる 
## ただ、closeするのを忘れやすい。。。
## → withを使って、ファイル参照の開始・終了を自動コントロールするのがおすすめ

with open(file_path, mode="r",encoding="utf-8") as f:
    lines = f.readlines()
    print(lines) 

print(f.read()) ## ファイルを閉じているため、参照エラーとなる