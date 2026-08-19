import sys

input = sys.stdin.readline
output = []

n , find = map(int, input().split())
hm = dict()

for i in range(n):
    name = input().strip()
    hm[name] = str(i+1)
    hm[str(i+1)] = name


for _ in range(find):
    x = input().strip()
    output.append(hm[x])

sys.stdout.write("\n".join(output))
