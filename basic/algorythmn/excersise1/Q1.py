## 1950年から2050年までのあいだにある「うるう年」を出力するプログラムを作成してください
## 閏年の判定条件 : 4で割り切れる年は、うるう年. ただし, 100で割り切れて400で割り切れない年は、うるう年ではない

uruu_year = []

# def check_year(year):

#     if (year % 4 == 0) :

#         uruu_year.append(year)

#     elif (year % 100 == 0) and (year % 400 == 0):

#         uruu_year.append(year)

for year in range(1950,2050+1):
    
    if (year % 4 == 0) :

        uruu_year.append(year)

    elif (year % 100 == 0) and (year % 400 == 0):
        
        uruu_year.append(year)

print(uruu_year)