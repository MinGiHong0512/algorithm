import heapq

pq = []
answer = []

repeat = int(input())

for i in range(repeat):
    heapq.heappush(pq, int(input()))

    temp = []
    mid_index = len(pq) // 2

    if mid_index % 2 == 0:
        mid_index -= 1


    for _ in range(i // 2):
        temp.append(heapq.heappop(pq))

    mid_value = heapq.heappop(pq)
    temp.append(mid_value)
    answer.append(mid_value)

    for num in temp:
        heapq.heappush(pq, num)

print()
for num in answer:
    print(num)