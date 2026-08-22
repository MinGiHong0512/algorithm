def solution(t, p):
    answer = 0

    p_len = len(p)

    m = 10 ** p_len

    for i in range(len(t)- p_len + 1):
        n = int(t[i:i+p_len])

        if (int(p) >= n):
            answer += 1        

    return answer


t, p = input().split()

print(solution(t,p))