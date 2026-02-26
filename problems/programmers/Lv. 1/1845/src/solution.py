from collections import Counter
def solution(nums):

    n = len(nums)
    count = Counter(nums)



    answer = len(count.keys())  if len(count.keys()) < n // 2 else n // 2
    return answer