n = int(input())

ATM_list = [int(i) for i in input().split()]

total_time = 0

ATM_list.sort()

for i in range(n):
    if(i == 0):
        total_time += ATM_list[0]
    else:
        ATM_list[i] = ATM_list[i] + ATM_list[i-1]
        total_time += ATM_list[i]

print(total_time)