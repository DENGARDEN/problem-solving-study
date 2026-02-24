from collections import Counter

def solution(participant, completion):
    cnt = Counter(participant)
    for name in completion:
        cnt[name] -= 1
    return next(name for name, v in cnt.items() if v > 0)