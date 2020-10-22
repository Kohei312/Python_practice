# 論理型, OR, AND

## if文を書くときは、末尾に : を振る

animal = True
mammal = True
insect = True

if animal and mammal:
    print("動物です")

if animal and insect:
    print("昆虫です")
else:
    print("そのほかの生き物です")