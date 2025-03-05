# My solution
def solution(numer1, denom1, numer2, denom2):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    answer = [numer1 * denom2 + numer2 * denom1, denom1 * denom2]

    current_gcd = gcd(answer[0], answer[1])
    answer[0] //= current_gcd
    answer[1] //= current_gcd

    return answer
