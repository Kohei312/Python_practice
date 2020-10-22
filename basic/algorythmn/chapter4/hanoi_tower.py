## ハノイの塔

n = int(input()) ## 円盤の段数


def hanoi_tower(n, st, dis, via):

    if n > 1:
        print("nは : {}".format(n))
        hanoi_tower(n - 1, st, via, dis) ## そのほかの円盤の、再帰処理
        
        print("st : {} => dis : {}, n = {}".format(st,dis,n))

        hanoi_tower(n - 1, via, dis, st) ## 再帰処理
    
    else:

        print("st : {} => dis : {}, n = {}".format(st,dis,n))

hanoi_tower(n, "a","b","c")