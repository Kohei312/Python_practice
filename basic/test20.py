## ループ内処理（continue, break, else）

### continue : 処理を1度とばす
# for i in range(10):
#     if i == 3:
#         continue
#     print(i) # ここの処理が飛ばされる

### break : 処理を止めて、ループ外に出る
# for i in range(10):
#     if i == 3:
#         break # ここで処理終了、ループ外へ
#     print(i)

### else : python独自の処理。ループ処理を抜けた場合に実行される(*** breakで出た場合は実行されない ***)
# for i in range(10):
#     print(i)
# else:
#     print("処理終了")