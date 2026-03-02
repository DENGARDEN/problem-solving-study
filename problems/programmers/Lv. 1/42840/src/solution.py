from itertools import cycle

def solution(answers):
    patterns = [
        cycle([1, 2, 3, 4, 5]),
        cycle([2, 1, 2, 3, 2, 4, 2, 5]),
        cycle([3, 3, 1, 1, 2, 2, 4, 4, 5, 5]),
    ]
    
    scores = [0, 0, 0]
    for ans in answers:
        for j, gen in enumerate(patterns):
            if ans == next(gen):
                scores[j] += 1
    
    max_score = max(scores)
    return sorted([i + 1 for i in range(3) if scores[i] == max_score])