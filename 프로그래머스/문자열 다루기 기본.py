def solution(s):
    answer = False

    if len(s) == 4 or len(s) == 6:
        for i in range(len(s)):
            if 0 <= (ord(s[i]) - ord('0')) <= 9:
                answer = True
            else:
                answer = False
                return answer

    return answer

x = input()

print(solution(x))