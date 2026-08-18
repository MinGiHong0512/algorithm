def solution(message, spoiler_ranges):
    answer = 0

    word_list = [item for item in message.split()]

    word_len_list = [[0 for _ in range(2)] for _ in range(len(word_list))]

    for i in range(len(word_list)):
        if i == 0:
            word_len_list[i][0] = i
        else: 
            word_len_list[i][0] = word_len_list[i-1][1] + 2
        
        word_len_list[i][1] = word_len_list[i][0] + len(word_list[i]) - 1

    print(word_len_list)

    return answer



message = input()
arr = list(map(int, input().split()))

spoiler_ranges = []

for i in range(len(arr)//2):
    for j in range(2):
        temp_list = []
        temp_list.append(arr[i*2+j])
    
    spoiler_ranges.append(temp_list)


print(solution(message, spoiler_ranges))