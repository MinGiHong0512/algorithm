import math

num = (123456 * 2 )
prime = [True] * (num+1)

prime[0] = prime[1] = False

for i in range(2,int(math.sqrt(num))+1):
    if  prime[i]:
        for j in range(i * i , num +1, i):
            prime[j] = False

while True:
    n = int(input())
    if n == 0:
        break
    print(sum(prime[n+1: n*2+1]))
