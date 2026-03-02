from functools import cmp_to_key

def solution(numbers):
    nums = list(map(str, numbers))
    nums.sort(key=cmp_to_key(lambda x, y: -1 if x+y > y+x else 1))
    answer = ''.join(nums)
    return answer if answer[0] != '0' else '0'