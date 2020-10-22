## 西暦の年んが引数で与えられた時、元号に変換して出力する関数を作成してください。
## 与えられる西暦の年は、1869以上 2020以下

## 1868 ~ 1911 : 明治
## 1912 ~ 1925 : 大正
## 1926 ~ 1988 : 昭和
## 1989 ~ 2019 : 平成
## 2019 ~      : 令和

meiji_year = [m for m in range(1868,1912+1)]
taisho_year = [t for t in range(1913,1926+1)]
showa_year = [s for s in range(1926,1989+1)]
heisei_year = [h for h in range(1990,2019+1)]
reiwa_year = [r for r in range(2019,2020+1)]

def check_year(year):

        if 1868 <= year < 1912:
            ## 配列の何番目にあたるか
            japanese_century = meiji_year.index(year)
            print(meiji_year)
            return "明治 {} 年".format(japanese_century + 1)   

        elif 1912 <= year < 1926:
            ## 配列の何番目にあたるか
            japanese_century = taisho_year.index(year)
            return "大正 {} 年".format(japanese_century + 1)   

        elif 1926 <= year < 1989:
            ## 配列の何番目にあたるか
            japanese_century = showa_year.index(year)
            return "昭和 {} 年".format(japanese_century + 1)   

        elif 1989 <= year <= 2019:
            ## 配列の何番目にあたるか
            japanese_century = heisei_year.index(year)
            return "平成 {} 年".format(japanese_century + 1)   

        elif 2019 <= year :
            ## 配列の何番目にあたるか
            japanese_century = reiwa_year.index(year)
            return "令和 {} 年".format(japanese_century + 1)   

print(check_year(1954))