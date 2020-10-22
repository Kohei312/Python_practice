import keyword
import pprint

# データ構造

# 定数：すべて大文字で記述するのがマナー
## (pythonでは、厳密に定数を定義することができないため)

KING_ANIMAL = "Lion"
animal = "dog"

# 変数の展開方法（全世代共通）
print('animalは, {}'.format(animal))

# python 3.6以降のprint文内での変数展開の書き方
# print(f'{animal}')

# python 3.8以降のprint文内での変数展開の書き方
## この書き方だと、変数が定義された行がすべて表示される
# print(f'{animal=}')



# 予約語の一覧
## pprint.pprint(keyword.kwlist, compact=True)

#　予約語かどうかの確認
## print(keyword.iskeyword('ここに文字列を入力する'))

LEGAL_AGE = 20
age = 18

if age < LEGAL_AGE:
    print("未成年")
else:
    print("成人")

print(f'age = {age}')