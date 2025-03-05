# My solution
def solution(my_string, n):
    answer = "".join([s * n for s in my_string])
    return answer