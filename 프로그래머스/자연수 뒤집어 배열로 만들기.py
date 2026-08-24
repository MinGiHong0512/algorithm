import sys

def solution(n):
    answer = []

    while n > 0:
        answer.append(n%10)
        n //= 10

    return answer

input = sys.stdin.readline().rstrip()

n = int(input)

print(solution(n))