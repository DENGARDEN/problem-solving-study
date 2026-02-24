def solution(str1, str2):
    answer = str1.split(str2)
    if len(answer) == 1:
        return 2
    else :
        return 1
