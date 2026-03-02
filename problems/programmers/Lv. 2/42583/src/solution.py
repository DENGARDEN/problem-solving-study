from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    on_bridge = deque()
    on_hold = deque(truck_weights)
    current_weight = 0

    while on_bridge or on_hold:
        answer += 1

        if len(on_bridge) == bridge_length:
            current_weight -= on_bridge.popleft()

        if on_hold and current_weight + on_hold[0] <= weight:
            truck = on_hold.popleft()
            on_bridge.append(truck)
            current_weight += truck
        else:
            on_bridge.append(0)

        if current_weight == 0:
            break

    return answer