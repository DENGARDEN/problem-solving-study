from collections import defaultdict, deque

def solution(n, wires):
    graph = defaultdict(list)
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    def bfs(start, blocked_v1, blocked_v2):
        """blocked 간선을 제외하고 start에서 도달 가능한 노드 수"""
        visited = set([start])
        queue = deque([start])
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor in visited:
                    continue
                if (node == blocked_v1 and neighbor == blocked_v2) or \
                   (node == blocked_v2 and neighbor == blocked_v1):
                    continue
                visited.add(neighbor)
                queue.append(neighbor)
        return len(visited)

    answer = n  # 최대 차이값으로 초기화
    for v1, v2 in wires:
        count = bfs(v1, v1, v2)
        answer = min(answer, abs(count - (n - count)))
    return answer