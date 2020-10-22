# lambda式(無名関数)
## 1行で終わるような処理を、簡潔に書く関数

## ex) x = 0 if y > 10 else 1
## 以下と同義 
## if y > 10:
##     return x = 0
## else:
##     return x = 1

## lambdaで書き換えると, lambda = 引数:返り値 なので
## x = lambda y: 0 if y > 10 else 1

# y = 10 
# x = 0 if (y-20) > 0 else 1 
# print(x)

# lambda_a = lambda x :x * x 
# print(lambda_a(10)) # 100

lambda_b = lambda x,y,z=5:x*y*z
# print(lambda_b(2,3)) # x=2,y=3, 30
# print(lambda_b(2,3,4)) # x=2,y=3, z=4 24

lambda_c = lambda x,y: y if x < y else x # if(x<y) => y, else x
print(lambda_c(2,4)) # 4