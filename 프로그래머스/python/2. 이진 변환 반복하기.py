def solution(s):
    answer = []
    
    zero_count = 0
    parse_count = 0
    
    while True:
        
        if len(s) == 1:
            answer.append(parse_count)
            answer.append(zero_count)
            break
            
        parse_count += 1
        
        temp = ""
        
        for i in range(len(s)):
            if s[i] == "0":
                zero_count += 1
            else:
                temp += "1"
                
        
        s = temp
        
        temp = ""
        
        idx = len(s)
        
        while idx > 1:
            temp += str(idx%2)
            idx //= 2
            
        temp+="1"
        
        s = temp[::-1]
            
            
    
        
    return answer