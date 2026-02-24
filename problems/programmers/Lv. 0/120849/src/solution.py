def solution(my_string):
    answer = ''
    for x in my_string:
        if x not in ['a', 'e', 'i', 'o', 'u']:
            answer += x
    return answer