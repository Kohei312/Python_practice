## 10進数を2進数で表現する

# n = 18 # 対象の10進数

# result = ''


# while n > 0:
#     result = str(n % 2) + result ## ここで2進数表現に変換している
#     n //= 2
#     print("n : {}, result : {}".format(n,result))

# print("result :{}".format(result))




## 基数を指定したバージョン

# n = 18 

# base = int(input("なに進数で計算しますか？"))


# def convert(n,base):

#     result = ""

#     while n > 0:
#         result = str(n % base) + result
#         n //= base

#     return result

# print(convert(n,base))