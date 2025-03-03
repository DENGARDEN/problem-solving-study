# 85.7 / 100.0
# # My solution
# def solution(n):
#     from functools import reduce

#     answer = reduce(lambda x, y: x + y, range(2, n + 1, 2))   # Error : if n is 1, the range is empty
#     return answer


# 100.0 / 100.0
# Other solution
def solution(n):
    return sum(range(2, n + 1, 2))
