import heapq

def solution(jobs):
    n = len(jobs)
    # (요청시각, 소요시간, 원래 번호)
    jobs = sorted((s, l, i) for i, (s, l) in enumerate(jobs))
    
    time = 0
    total = 0
    heap = []
    idx = 0
    done = 0
    
    while done < n:
        # 현재 시각까지 도착한 작업을 힙에 push (소요시간, 요청시각, 번호)
        while idx < n and jobs[idx][0] <= time:
            s, l, i = jobs[idx]
            heapq.heappush(heap, (l, s, i))
            idx += 1
        
        if heap:
            l, s, i = heapq.heappop(heap)
            time += l
            total += time - s  # 반환 시간
            done += 1
        else:
            # 대기 작업이 없으면 다음 작업 요청 시각으로 점프
            time = jobs[idx][0]
    
    return total // n