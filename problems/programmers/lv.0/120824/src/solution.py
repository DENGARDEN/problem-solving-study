# My solution
# Potential undercountning when n is 0; bool(0) is False
# def solution(num_list):

#     answer = [
#         sum([bool(n) for n in num_list if n % 2 == 0]),
#         sum([bool(n) for n in num_list if n % 2 == 1]),
#     ]
#     return answer


# My solution
def solution(num_list):

    return [sum(n % 2 == 0 for n in num_list), sum(n % 2 == 1 for n in num_list)]
