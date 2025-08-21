re = int(input().rstrip())
totalApple : int = 0
totalPrice : int = 0
totalWeight : int = 0
for i in range(re):
    box,w, h, l = map(str , input().split())
    w = int(w)
    h = int(h)
    l = int(l)
    if(box == "A"):
        totalApple  += (w//12) * (h // 12) * (l // 12)
        totalWeight += 1000
    else:
        totalWeight += 6000
totalWeight += (totalApple * 500)
totalPrice = totalApple * 4000

print(totalWeight)
print(totalPrice)