import heapq

def solution(numbers):
    max_heap = [-n for n in numbers]
    heapq.heapify(max_heap)
    a = -heapq.heappop(max_heap)
    b = -heapq.heappop(max_heap)
    return a * b