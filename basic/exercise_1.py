## 演習問題

## 1
num = 10

## 2
# print(num)

## 3
num_str = str(num)
# print(num_str)

## 4
num_list = [num_str,'20','30']
# print(num_list)

## 5
num_list.append('40')
# print(num_list)

## 6
num_tuple = tuple(num_list)
# print(num_tuple)

## 7
# value = input() # コンソール上に値を入力できる
# num_tuple += (value,)
# print(num_tuple)

## 8
num_set = {'40','50','60'}
# print(num_set) 

## 9
u = set(num_tuple) | num_set 
# print(u)

## 10
num_dict = {num_tuple:num_str}
# print(num_dict)


## 11
l = len(num_list)
# print(l)

## 12
# print(num_dict.get("MyKey","Does not exist"))

## 13
num_list.extend(["50","60"])
# print(num_list)
### 以下も同義
# new_list = num_list + ["50","60"]
# print(new_list) 


## 14
# val = input()
# is_under_50 = int(val) < 50
# print(is_under_50)

## 15
# print(f'num_str = {num_str}')

### 以下と同義
# num_str = set(num_str)
# print(num_str)

## 16
# print(dir(num_dict))