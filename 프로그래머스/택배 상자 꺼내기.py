def solution(n, w, num):
    answer = 0

    n -= 1
    num -=1

    dir_top = 0
    dir_bottom = 0

    dir_top = n // w
    dir_bottom = num // w

    answer = dir_top - dir_bottom

    if dir_top % 2 == dir_bottom % 2:
        if n % w >= num % w:
            answer += 1
    else:
        if n % w + num % w >= w - 1:
            answer+=1


    return answer

n, w, num = map(int, input().split())

print(solution(n,w,num))