repeat = int(input())
for i in range(repeat):
    s = input()
    total = 0
    add : int = 0
    for j in range(len(s)):
        if s[j] == "O":
            add +=1
            total += add 
        else :
            add = 0
    print(total)