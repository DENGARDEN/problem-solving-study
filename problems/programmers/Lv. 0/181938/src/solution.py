def solution(a: int, b: int) -> int:
    answer: int = 0

    x = int(str(a) + str(b))
    y = 2 * a * b

    if x > y:
        answer = x
    elif y > x:
        answer = y
    else:
        answer = x

    return answer