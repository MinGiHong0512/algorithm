def solution(survey, choices):
    answer = ''

    score_list = [0 for _ in range(4)]

    plus_list = ["R","C","J","A"]
    minus_list = ["T","F","M","N"]
    zero_list = ["R","C","J","A"]

    for i in range(len(survey)):
        print(score(choices[i]))
        for j in range(4):
            s = score(choices[i])
            if survey[i][0] == plus_list[j]:
                if choices[i] > 4:
                    s *= -1
                score_list[j] += s
                    
            elif survey[i][0] == minus_list[j]:
                if choices[i] > 4:
                    s *= -1
                score_list[j] -= s

    print(score_list)

    for i in range(4):
        if score_list[i] < 0:
            answer += minus_list[i]
        elif score_list[i] > 0:
            answer += plus_list[i]
        elif score_list[i] == 0:
            answer += zero_list[i]

    return answer

def score(s):

    value = s

    if s < 4:
        value = (value * -1) + 4
    elif s > 4:
        value = s % 4
    else:
        value = 0 
  
    return value
    

survey = input().split()
choice = list(map(int,input().split()))

print(solution(survey,choice))