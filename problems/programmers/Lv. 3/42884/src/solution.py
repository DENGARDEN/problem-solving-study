def solution(routes):
    routes.sort(key=lambda x: x[1])  
    camera = -30001  
    count = 0
    
    for enter, exit in routes:
        if enter > camera:  
            camera = exit   
            count += 1
    
    return count