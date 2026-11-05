import math

repeat = int(input())

for i in range(repeat):
   
   n = int(input())
   log_sum = sum(math.log10(i) for i in range(1, n+1))
   digit_count = int(log_sum) + 1
   print(digit_count)  




