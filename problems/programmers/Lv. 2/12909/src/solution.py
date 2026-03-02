def solution(s):    
    answer = True

    stack = []

    for c in s:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if not stack:
                answer = False
                break
            stack.pop()
    
    if stack:
        answer = False
    
    return answer