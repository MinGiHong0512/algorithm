import heapq
import sys

input = sys.stdin.readline
output = []

pq = heapq()

n = int(input())



for _ in range(n):
    x = int(input())
    if(x == 0):
        output.append(heapq.heappop(pq))
    else:
        heapq.heappush(pq , 2 ** 32 - x , x)

sys.stdout.write("\n".join(output))