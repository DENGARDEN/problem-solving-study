from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    nums = set()
    for length in range(1, len(numbers) + 1):
        for perm in permutations(numbers, length):
            nums.add(int(''.join(perm)))

    return sum(1 for n in nums if is_prime(n))