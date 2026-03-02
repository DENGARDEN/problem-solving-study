from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for perm in permutations(dungeons):
        fatigue, count = k, 0
        for req, cost in perm:
            if fatigue >= req:
                fatigue -= cost
                count += 1
        answer = max(answer, count)
    return answer