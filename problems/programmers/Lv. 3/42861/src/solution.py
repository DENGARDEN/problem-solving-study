def solution(n, costs):
    costs.sort(key=lambda x: x[2])

    parent = list(range(n))
    rank = [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra==rb:
            return False
        
        if rank[ra] < rank[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] +=1
        return True
    
    total_cost = 0
    edges_used = 0

    for u, v, cost in costs:
        if union(u, v):
            total_cost += cost
            edges_used += 1
            if edges_used == n - 1:
                break
    
    return total_cost
    