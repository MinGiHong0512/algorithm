repeat = int(input())
zero = [0] * (40 + 1)
one = [0] * (40 + 1)

zero[0] = 1
zero[1] = 0

one[0] = 0
one[1] = 1

for i in range(2 , 40 + 1):
    one[i] = one[i-1] + one[i-2]
    zero[i] = zero[i-1] + zero[i-2]

for _ in range(repeat):
    n = int(input())
    print(zero[n], one[n])