def solution(n):
    answer = 0
    
    fib = [0 for _ in range(n+1)]
    
    fib[0] = 0
    fib[1] = 1
    
    
    for i in range(2,n+1):
        fib[i] = fib[i-1] + fib[i-2]    
    
    
    answer = fib[len(fib)-1] % 1234567
    
    return answer