# 演算の続き

value = 10

# 四則演算の省略した書き方
# value += 3
# value -= 5
# print(value)

# 浮動小数点数
# height = 175.6 
# print(type(height)) #typeをつけてprintすると、型を確認できる
# print(height + 10) # float型の値と、Int型の値を組み合わせて計算することも可能

print(12 & 21) # 01100 and 10101 = 00100 => 4
print(12 | 21) # 01100 or 10101 = 11101 => 29
## これも省略して記述可能
value = 12
value &= 21
## 計算後の結果がprintされる
print(value)