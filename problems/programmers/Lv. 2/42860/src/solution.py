def solution(name):
    updown = 0
    for c in name:
        x = ord(c) - ord('A')
        updown += min(x, 26 - x)
    
    n = len(name)
    move = n - 1
    
    for i in range(n):
        next_idx = i + 1
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
        
        move = min(move, 2 * i + (n - next_idx)) # R L R
        move = min(move, 2 * (n - next_idx) + i) # L R L
    
    return updown + move