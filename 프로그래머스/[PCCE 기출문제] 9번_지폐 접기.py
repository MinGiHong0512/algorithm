import sys

input = sys.stdin.readline

def solution(wallet, bill):
    answer = 0

    while True:

        if (wallet[0] >= bill[0] and wallet[1] >= bill[1]) or (wallet[1] >= bill[0] and wallet[0] >= bill[1]):
            break

        if bill[0] > bill[1]:
            bill[0] //= 2
        else:
            bill[1] //= 2
        answer += 1
        print(bill)
    

    return answer


wallet = list(map(int,input().split()))
bill = list(map(int,input().split()))

print(solution(wallet=wallet, bill=bill))