## 制御文
# if 評価式1:
#     式 # 評価式1がTrueの場合
# elif 評価式2:
#     式 # 評価式1がFalseで、かつ評価式2がTrueの場合
# else:
#     式 # 評価式1,2ともFalseの場合

# msg = 'blue'

# if msg == 'blue':
#     print("すすむ")
# elif msg == 'red':
#     print("止まる")
# else:
#     print("ゆっくりすすむ")

# age = 70

# if age < 20:
#     print("20未満")
# elif age <= 40: # 20以上で実行
#     print("20以上40以下")
# elif age >= 60:
#     print("60以上です")
# else :
#     print("その他")

## 条件分岐の書き方 ： and, or, not
### and
# 評価式1 and 評価式2 # 評価式1,2とも正しい場合
# ### or 
# 評価式1 or 評価式2 # 評価式1,2のどちらかが正しい場合
# ### not 
# not 評価式 # 評価式が誤っている場合


gender = "man"
age = 30

# if gender == "man" and age < 20:
#     print("未成年男性です")

# if gender == "man" or age < 20:
#     print("未成年または男性です")

# if not gender == "man":
#     print("男性ではない")

# if gender != "man":
#     print("男性ではない")

