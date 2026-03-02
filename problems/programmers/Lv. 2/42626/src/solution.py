import heapq

def solution(scoville, K):
    heapq.heapify(scoville)          # O(n) 으로 힙 구성 (in-place)
    count = 0

    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        first = heapq.heappop(scoville)   # 가장 안 매운 음식
        second = heapq.heappop(scoville)  # 두 번째로 안 매운 음식
        new = first + second * 2
        heapq.heappush(scoville, new)
        count += 1

    return count