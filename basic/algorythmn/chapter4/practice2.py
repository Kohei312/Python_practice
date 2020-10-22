## pref_dataの並びに影響を受けて誤差発生...

pref_data = {
    "北海道": 5381733,
    "宮城県": 2333899,
    "福島県": 1914039,
    "群馬県": 1973115,
    "東京都": 12515271,
    "富山県": 1066328,
    "山梨県": 834930,
    "静岡県": 3700305,
    "滋賀県": 1412916,
    "兵庫県": 5534800,
    "鳥取県": 573441,
    "広島県": 2843990,
    "香川県": 976263,
    "福岡県": 5101556,
    "熊本県": 1786170,
    "鹿児島県": 1648177,
    "青森県": 1308265,
    "秋田県": 1023119,
    "茨城県": 2916976,
    "埼玉県": 7266534,
    "神奈川県": 9126214,
    "石川県": 1154008,
    "長野県": 2098804,
    "愛知県": 7483128,
    "京都府": 2610353,
    "奈良県": 1364316,
    "島根県": 694352,
    "山口県": 1404729,
    "愛媛県": 1385262,
    "佐賀県": 832832,
    "大分県": 1166338,
    "沖縄県": 1433566,
    "岩手県": 1279594,
    "山形県": 1123891,
    "栃木県": 1974255,
    "千葉県": 6222666,
    "新潟県": 2304264,
    "福井県": 786740,
    "岐阜県": 2031903,
    "三重県": 1815865,
    "大阪府": 8839469,
    "和歌山県": 963579,
    "岡山県": 1921525,
    "徳島県": 755733,
    "高知県": 728276,
    "長崎県": 1377187,
    "宮崎県": 1104069,
}

pref = list(pref_data.values())
pref_items = []

goal = 10000000

min_total = 0

def search(total,pos):
    global min_total


    ## 辞書内の数を超えない範囲で計算
    if pos >= len(pref):
        return 

    if total < goal:
        
        ## abs関数 : 絶対数を返す関数
        ## 絶対値（目標値 - (total + 選んだ県の人口)） < 絶対値（目標値 - min_total） かどうか
        if abs(goal - (total + pref[pos])) < abs(goal - min_total):
            
            ##  total + 選んだ県の人口が, min_totalに
            min_total = total + pref[pos]
            pref_items.append(pref[pos])

            ## total + 選んだ県の人口, posを1つ増やして再帰
            search(total + pref[pos], pos + 1)

        search(total, pos + 1)

def inverse_dict(d,items):
    for item in items:
        for k,v in d.items():
            if v == item:
                pref_name.append(k) 


search(0,0)
print(min_total)

pref_name = []
inverse_dict(pref_data,pref_items)

print(pref_name)