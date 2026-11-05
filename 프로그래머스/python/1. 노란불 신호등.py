def solution(signals):
    answer = 0

    sum_list = [0 for _ in range(len(signals))]


    for i in range(len(signals)):
        for j in signals[i]:
            sum_list[i] += j
        if sum_list[i] > 20:
            return -1

    limit = sum_list[0]

    for i in range(len(signals)-1):
        limit = LCM(limit, sum_list[i+1])

    for i in range(1, int(limit)):

        yellow = True

        for j in range(len(signals)):
            n = i % sum_list[j] - signals[j][0] - 1

            if i == 43:
                print(n)

            if 0 > n or  n >= signals[j][1]:
                yellow = False
            

        if yellow:
            return i

    return -1

def LCM(a,b):
    return (a*b)/GCD(a,b)


def GCD(a,b):
    if b <= 0:
        return a
    if a > b:
        temp = a
        a = b
        b = temp

    return GCD(a, b%a)    
    

arr = list(map(int, input().split()))

signals = []


for i in range(len(arr)//3):
    temp_signals = [0 for _ in range(3)]
    for j in range(3):
        temp_signals[j] = arr[i*3 + j]

    signals.append(temp_signals)


print(int(solution(signals)))