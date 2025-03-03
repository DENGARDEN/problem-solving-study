# Best solution from other users


def solution(n):
    return sum([i for i in range(2, n + 1, 2)])


def solution(n):
    return 2 * (n // 2) * ((n // 2) + 1) / 2
