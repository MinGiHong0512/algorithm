def solution(s):
    answer = ''

    s = list(s)

    if len(s) == 0:
         return answer

    if s[0] != ' ':
        c =  ord(s[0])
        if 0 <= (c-ord('0')) <= 9:
            s[0] = chr(c)
        elif not 65 <= c <= 90:
                s[0] = chr(c-32)

    for i in range(1, len(s)):

        c = ord(s[i])

        if 0 <= (c-ord('0')) <= 9:
            s[i] = chr(c)
        elif s[i-1] == ' ' and s[i] != ' ':
            if not 65 <= c <= 90:
                s[i] = chr(c-32)
        elif 65 <= c <= 90:
            s[i] = chr(c+32)
        
    return answer.join(s)

s = input()

print(solution(s))