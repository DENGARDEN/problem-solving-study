from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    
    queue = deque()
    for p, s in zip (progresses, speeds):
        queue.append((math.ceil((100-p)/s)))    # 남은 일 수

    while queue:

        front = queue.popleft() # 이번 배포 남은 일 수
        count = 1 # 기준 작업 수
        
        while queue and front >= queue[0]:  # 기준 작업보다 남은 일 수가 더 적은 작업이 있다면
            queue.popleft()
            count += 1
        
        answer.append(count)

    return answer