import sys

input = sys.stdin.readline
write = sys.stdout.write

n = int(input())

s = [0 for _ in range(20)]

output = []

for _ in range(n):
    number = 0
    cmd = input().split()
    
    if len(cmd) == 2:
        temp , number = cmd
        number = int(number) - 1
    else:
        temp = cmd[0]

    if temp == "add":
        s[number] = 1
    elif temp == "remove":
        s[number]=0
    elif temp =="check":
        write("1\n" if s[number] == 1 else "0\n")
    elif temp == "toggle":
        s[number] = 1 - s[number]
    elif temp == "all":
        s = [1 for _ in range(20)]
    elif temp == "empty":
        s = [0 for _ in range(20)]
