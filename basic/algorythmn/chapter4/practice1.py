
## 1 ・ 10 階 の組み合わせは除外（最後に +１する）
## 1 ・ 10 階 に至る, 2~9階の組み合わせを考える

data = [2,3,4,5,6,7,8,9]

# def combinationWithRepetitionListRecursive(data):

#   result = []
#   _combinationWithRepetitionListRecursive(data, 0, [], result)
#   return result

# ## スタート位置を指定
# def _combinationWithRepetitionListRecursive(data, start, progress, result):
#   data.pop()
  
#   if data == []:
#     result.append(progress)
#     return

  
#   for i in range(start, len(data)):
#     _combinationWithRepetitionListRecursive(data, i, progress + [data[i]], result)

# total = len(combinationWithRepetitionListRecursive(data))
# print(total + 1)