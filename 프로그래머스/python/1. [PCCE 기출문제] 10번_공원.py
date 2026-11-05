def solution(mats, park):
    answer = 0
    
    for item in sorted(mats,reverse=True):
        for i in range(len(park)-item+1):
            for j in range(len(park[i])-item+1):
                if park[i][j] == "-1":
                    check = True
                    
                    for k in range(item):
                        if not check:
                            break
                        for l in range(item):
                            if park[i+k][j+l] != "-1":
                                check=False
                    if check and answer == 0:
                        answer = item
                    
    if answer == 0:
        answer = -1
    
    return answer

