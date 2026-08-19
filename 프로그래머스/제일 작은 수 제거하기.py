def solution(arr):
    answer = []

    if len(arr) == 1:
        answer.append(-1)
        return answer
    
    n = arr[0]

    for i in arr:
        if n > i:
            n = i
    
    arr.remove(n)
    answer = arr

    return answer

arr = list(map(int, input().split()))

print(solution(arr))