from itertools import combinations

repeat , r = map(int, input().split())

data = []
for i in range(repeat):
    data.append(i+1)

for comb in combinations(data, r):
    print(" ".join(map(str,comb)))
