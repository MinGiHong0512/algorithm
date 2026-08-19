n , price = map(int , input().split())
coin = []

for _ in range(n):
    p = int(input())
    coin.append(p)

coin.sort()
coin.reverse()

totalPrice = price
count = 0

for i in coin:
    if totalPrice >= i:
        count += totalPrice // i
        totalPrice%=i
print(count)