import heapq

pq = []
answer = []

repeat = int(input())

for i in range(repeat):
    heapq.heappush(pq, int(input()))

    temp = []
    for _ in range(i // 2):
        temp.append(heapq.heappop(pq))

    mid_value = heapq.heappop(pq)
    temp.append(mid_value)
    answer.append(mid_value)

    for num in temp:
        heapq.heappush(pq, num)

for num in answer:
    print(num)