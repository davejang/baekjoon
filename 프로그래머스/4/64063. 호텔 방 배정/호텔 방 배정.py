import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

def find_room(room, number):
    if room[number] == 0:
        room[number] = number + 1
        return number
    else:
        room[number] = find_room(room,room[number])
        return room[number]

def solution(k, room_number):
    room = defaultdict(lambda: 0)
    answer = []
    
    for i in room_number:
        answer.append(find_room(room,i))
    
    return answer