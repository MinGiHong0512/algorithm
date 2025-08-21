def mod_pow(a, b, c):
    if b == 0:
        return 1
    half = mod_pow(a, b // 2, c)
    half = (half * half) % c
    if b % 2 == 0:
        return half
    else:
        return (half * (a % c)) % c


a, b, c = map(int, input().split())
print(mod_pow(a, b, c))