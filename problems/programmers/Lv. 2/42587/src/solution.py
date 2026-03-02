from collections import deque

def solution(priorities, location):
    answer = 0
    
    queue = deque()
    for  i in range(len(priorities)):
        queue.append((i, priorities[i]))

    while queue:
        idx, priority = queue.popleft() # execute now?
        if not queue or priority >= max(queue, key=lambda x: x[1])[1]:  # if priority is the highest
            answer += 1 # Execute count ++
            if idx == location: # This is the target
                break
        else:
            queue.append((idx, priority))
    
    return answer