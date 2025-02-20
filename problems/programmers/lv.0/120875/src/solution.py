# My solution
def solution(dots):
    def is_parallel(line1, line2):
        (x1, y1), (x2, y2) = line1
        (a1, b1), (a2, b2) = line2
        return (y2 - y1) * (a2 - a1) == (b2 - b1) * (x2 - x1)
    
    
    return 1 if (
        is_parallel([dots[0], dots[1]], [dots[2], dots[3]]) or
        is_parallel([dots[0], dots[2]], [dots[1], dots[3]]) or
        is_parallel([dots[0], dots[3]], [dots[1], dots[2]])
    ) else 0