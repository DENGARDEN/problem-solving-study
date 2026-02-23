def solution(sides):
    answer = sorted(sides, reverse=True)
    if answer[0] < answer[1] + answer[2]:
        return 1
    else:
        return 2