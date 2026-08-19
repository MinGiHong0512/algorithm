import heapq
import sys

input = sys.stdin.readline

pq  = []
output_arr = []
n = int(input())


for _ in range(n):
    idx = int(input())
    if idx == 0:
        if len(pq) != 0:
            priority , value = heapq.heappop(pq)
            output_arr.append(value)
        else:
            output_arr.append(0)
    else:
        heapq.heappush(pq,(abs(idx),idx))

sys.stdout.write("\n".join(map(str,output_arr)))