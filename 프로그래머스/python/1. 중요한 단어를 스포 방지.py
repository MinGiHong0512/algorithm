def solution(message, spoiler_ranges):
    answer = 0

    word_list = [item for item in message.split()]

    spoiler_word = set()

    bool_list = [False for _ in range(len(message.split()))]

    word_len_list = [[0 for _ in range(2)] for _ in range(len(word_list))]

    start_index = 1 if(message[0]==' ') else 0  

    for i in range(len(word_list)):
        if i == 0:
            word_len_list[i][0] = i + start_index
        else: 
            word_len_list[i][0] = word_len_list[i-1][1] + 2
        
        word_len_list[i][1] = word_len_list[i][0] + len(word_list[i]) - 1

    for i in range(len(word_len_list)):
        for j in spoiler_ranges:
            if word_len_list[i][0] <= j[1] and j[0] <= word_len_list[i][1]: 
                bool_list[i] = True
                spoiler_word.add(word_list[i])
                break

    for i in range(len(bool_list)):
        if bool_list[i] == False:
           if word_list[i] in spoiler_word:
                spoiler_word.discard(word_list[i])

    answer = len(spoiler_word)

    return answer



message = input()
arr = list(map(int, input().split()))

spoiler_ranges = []

for i in range(len(arr)//2):
    temp_list = []
    for j in range(2):
        temp_list.append(arr[i*2+j])
    
    spoiler_ranges.append(temp_list)

print(solution(message, spoiler_ranges))