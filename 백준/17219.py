n, find = map(int,input().split())

hm = dict()


for _ in range(n):
    key, value = input().split()
    hm[key] = value

for _ in range(find):
    temp = input()
    if temp in hm:
        print(hm[temp])