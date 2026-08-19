def solution(n):
    answer = []

    def hanoi(depth, start, mid ,end):

        if depth == 1:
            answer.append([start,end])
            return
        hanoi(depth-1,start, end,mid)

        answer.append([start,end])

        hanoi(depth-1, mid , start, end)


    hanoi(n, 1,2,3)


    return answer



n = int(input())

print(solution(n))