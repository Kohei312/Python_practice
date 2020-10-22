
# 与えられたデータ(listやtuple): data
# データの長さ: n
# 選ぶ数: r
# 重複あり順列の総数: H(n,r)
# 順列の総数: P(n,r)
# 重複あり組み合わせの総数: Π(n,r)
# 組み合わせの総数: C(n,r)

data = [1,2,3]
result = []

## 重複あり順列
# for i in range(len(data)):
#     for j in range(len(data)):
#         for k in range(len(data)):
#             result.append([data[i],data[j],data[k]])
#             print(result)

## 重複あり組み合わせ
# def listExcludedIndices(data, indices=[]):
#     return [ x for i, x in enumerate(data) if 1 not in indices ]

# for i in range(len(data)):
#     for j in range(i, len(data)):
#         for k in range(j, len(data)):
#             result.append([data[i],data[j],data[k]])
#             print(result)

## 重複なし組み合わせ
# def listExcludedIndices(data, indices=[]):
#     return [ x for i, x in enumerate(data) if 1 not in indices ]


# for i in range(len(data)):
#   for j in range(i + 1, len(data)):
#     for k in range(j + 1, len(data)):
#       result.append([data[i], data[j], data[k]])
#       print(result)

## 再帰版  重複あり順列
# def permutationWithRepetitionListRecursive(data, r):
#   if r <= 0:
#     return []

#   result = []
#   _permutationWithRepetitionListRecursive(data, r, [], result)
#   return result

# def _permutationWithRepetitionListRecursive(data, r, progress, result):
#   if r == 0:
#     result.append(progress)
#     return

#   for i in range(len(data)):
#     _permutationWithRepetitionListRecursive(data, r - 1, progress + [data[i]], result)

# print(permutationWithRepetitionListRecursive(data, 1))


## 再帰版 順列

# def permutationWithRepetitionListRecursive(data, r):
#   if r <= 0:
#     return []

#   result = []
#   _permutationWithRepetitionListRecursive(data, r, [], result)
#   return result

# def _permutationWithRepetitionListRecursive(data, r, progress, result):
#   if r == 0:
#     result.append(progress)
#     return

#   for i in range(len(data)):
#     _permutationWithRepetitionListRecursive(listExcludedIndices(data,[i]), r - 1, progress + [data[i]], result)

# def listExcludedIndices(data, indices=[]):
#     return [ x for i, x in enumerate(data) if 1 not in indices ]

# print(permutationWithRepetitionListRecursive(data, 3))

## 再帰版 重複あり組み合わせ

# def combinationWithRepetitionListRecursive(data, r):
#   if r <= 0:
#     return []

#   result = []
#   _combinationWithRepetitionListRecursive(data, r, 0, [], result)
#   return result

# ## スタート位置を指定
# def _combinationWithRepetitionListRecursive(data, r, start, progress, result):
#   if r == 0:
#     result.append(progress)
#     return

#   for i in range(start, len(data)):
#     _combinationWithRepetitionListRecursive(data, r - 1, i, progress + [data[i]], result)

# print(combinationWithRepetitionListRecursive(data, 3))


## 再帰版 組み合わせ
def combinationListRecursive(data, r):
  if r == 0 or r > len(data):
    return []

  result = []
  _combinationListRecursive(data, r, 0, [], result)
  return result


def _combinationListRecursive(data, r, start, progress, result):
  if r == 0:
    result.append(progress)
    return

  for i in range(start, len(data)):
    #別解 
    _combinationListRecursive(listExcludedIndices(data, [i]), r - 1, i, progress + [data[i]], result)


def listExcludedIndices(data, indices=[]):
    return [ x for i, x in enumerate(data) if 1 not in indices ]

print(combinationListRecursive(data, 3))


