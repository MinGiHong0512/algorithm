import sys

input = sys.stdin.readline().rstrip()

def solution(players, callings):
    dic_list = {}

    for i in range(len(players)):
        dic_list[players[i]] = i

    for calling in callings:
        index = dic_list[calling]

        players[index], players[index - 1] = players[index - 1], players[index]

        dic_list[players[index]] = index
        dic_list[players[index - 1]] = index - 1

    return players


players = list(input.split())

callings = list(input.split())

solution(players=players, callings=callings)