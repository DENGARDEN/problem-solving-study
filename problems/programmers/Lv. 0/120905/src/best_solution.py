def solution(n, numlist):
    answer = [i for i in numlist if i % n == 0]
    return answer


def solution(n, numlist):
    return list(filter(lambda v: v % n == 0, numlist))
