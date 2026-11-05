def solution(s):
    answer = ''
    
    number_list = [i for i in map(int,s.split())]
    
    MIN = sorted(number_list,reverse=False)[0]
    MAX = sorted(number_list,reverse=True)[0]
    
    answer = str(MIN) +" "+ str(MAX)
    
    return answer