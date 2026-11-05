def solution(food):
    answer = ''
    
    food_str = ""
    
    for i in range(1,len(food)):
        for j in range(food[i] // 2):
            food_str += str(i)
            
    food_str = food_str + "0" + food_str[::-1]
    
    answer = food_str
    
    return answer