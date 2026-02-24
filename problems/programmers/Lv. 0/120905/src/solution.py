def solution(n, numlist):
    answer = []
    for num in numlist: # O(n)
        if num % n == 0:
            answer.append(num)
    return answer