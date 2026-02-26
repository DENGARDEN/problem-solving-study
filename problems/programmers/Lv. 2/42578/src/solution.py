from collections import Counter
from functools import reduce

def solution(clothes):
    answer = {k: v + 1 for k, v in Counter(map(lambda x: x[1], clothes)).items()}
    return reduce(lambda x, y: x * y, answer.values()) - 1