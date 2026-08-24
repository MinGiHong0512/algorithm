import sys


def solution(n, m):
    answer = []

    LCM = 0
    GCD = 0

    N = n
    M = m

    while n != 0:
        n,m = m % n, n
    GCD = n

    LCM = (N * M) // GCD

    answer.append(GCD)
    answer.append(LCM)

    return answer

input = sys.stdin.readline().rstrip()

n,m = map(int,input.split())

print(solution(n,m))
