from queue import Queue

def bfs (n , target):
    visited = set()
    
    queue = Queue()
    queue.put((n,0))
    visited.add(n)

    while not queue.empty():
        tempNumber, count = queue.get()

        if tempNumber == target:
            return count
        for i in [tempNumber - 1, tempNumber + 1, tempNumber * 2]:
            if i not in visited and 0 <= i <= 2*target:
                visited.add(i)
                queue.put((i, count + 1))

n, target = map(int, input().split())
if n > target : 
    print(n - target)
else:
    print(bfs(n,target))
