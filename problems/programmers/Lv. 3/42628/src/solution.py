def solution(operations):
    answer = []
    for op in operations:
        if op[0] == 'I':
            answer.append(int(op[2:]))
        elif op[0] == 'D':
            if not answer:
                continue
            if op[2:] == '1':
                answer.remove(max(answer))
            else:
                answer.remove(min(answer))
    return [max(answer), min(answer)] if answer else [0, 0]


import heapq