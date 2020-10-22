## 10進数を2進数に変換する

# n = 10010
# print(bin(n)) ## 10 → 2進数へ変換

# num = str(n)
# print(int(num,2)) ## 2 → 10進数へ変換
# result = 0

# for i in range(len(num)):
#     print("len(num) : {}, num[i] : {}".format(len(num),num[i])) ## lengthは不変
#     # print(num[i]) ## 文字列numを、i番目から1文字ずつ取得
#     result += int(num[i]) * (2**(len(num) - i -1)) ## i=0 : 5けた - 0番目 - 1 = 4, i=1 : 5けた - 1番目 - 1 = 3, i=2 : 5けた - 2番目 - 1 = 2, i=3 : 5けた - 3番目 - 1 = 1, i=4 : 5けた - 4番目 - 1 = 0
#     print("result :{}".format(result)) ## 計算結果が足されていく

# print(result)

## ビット演算
a = 18
a_bin = bin(a) ## '0b10010'
# print(bin(~a)) ## '-0b10011' : 論理演算にて、一番左の値は正負反転の判断に用いられる. 
# print(int(a_bin,2))

b = 25
b_bin = 0b11001
# print(bin(b)) ##  '0b11001'

# print(bin(int(a_bin, 2) & b_bin)) ## 0b10000 論理積. int型で計算する(n進数のものを表現するときは、第二引数にnを入れることを忘れない!!)

# print(bin(int(a_bin, 2) | b)) ## 0b11011. 論理和

# print(bin(int(a_bin, 2) ^ b)) ## 0b101. 排他的論理和

# print(bin(int(a_bin, 2) << 1)) ## 0b100100. 左シフト

# print(bin(b >> 1)) ## 0b1100. 右シフト