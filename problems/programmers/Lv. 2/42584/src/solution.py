def solution(prices):
    n = len(prices)
    answer = [0 for _ in range(n)]
    stack = [] 

    for i in range(n):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    while stack:
        i = stack.pop()
        answer[i] = n - 1 - i

    return answer