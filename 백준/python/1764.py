repeat , nameCount = map(int, input().split())
name = set()
for _ in range(repeat):
    s = input()
    name.add(s)

count = 0
nameList = []
for _ in range(nameCount):
    s = input()
    if s in name :
        count += 1
        nameList.append(s)
print(count)
nameList.sort()
for i in range(count):
    print(nameList[i])
    