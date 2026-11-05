import sys

def solution(n):
    answer = 0

    n = (str(n))

    for i in range(len(n)):
        answer += int(n[i])

    return answer

input = sys.stdin.readline().rstrip()

N = input

print(solution(N))