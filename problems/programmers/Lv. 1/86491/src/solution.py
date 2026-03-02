def solution(sizes):
    answer = 0

    max_width = 0
    max_height = 0

    for size in sizes:
        width, height = size
        if width < height:
            width, height = height, width
        if width > max_width:
            max_width = width
        if height > max_height:
            max_height = height
    
    answer = max_width * max_height

    return answer