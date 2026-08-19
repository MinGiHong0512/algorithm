n = int(input())
temp =1
twos =0
fives = 0

for i in range(1,n+1):
    x =i
    while x % 2 == 0:
        x //= 2
        twos+=1
    while x % 5 == 0:
        x //= 5
        fives+=1

    temp = (temp * x) % 10

for _ in range(twos - fives):
    temp = (temp * 2) % 10

print(temp)