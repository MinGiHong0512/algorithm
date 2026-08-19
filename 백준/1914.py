def hanoi(start , temp, end,n):
    if n == 1:
        print(start , end)
        return
    
    hanoi(start , end, temp , n-1)
    print(str(start)+" "+str(end))
    hanoi(temp , start, end , n-1)

count = int(input())
print(2**count-1)
if count <= 20:
    hanoi(1, 2, 3, count)


