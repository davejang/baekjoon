from itertools import combinations
from math import prod

def solution(clothes):
    result = 1
    hashmap = {}
    hashmap_type = {}
    
    # 의상 정보에 대한 hashmap
    for item_list in clothes:
        hashmap[item_list[0]] = item_list[1]
     
    # 의상 종류 리스트
    clothes_type = list(hashmap.values())
    
    for type in clothes_type:
        if type in hashmap_type:
            hashmap_type[type] += 1
        else:
            hashmap_type[type] = 1
    
    type_list = list(hashmap_type.values())
    print(type_list)
    for i in type_list:
        result *= (i+1)
    
    return result - 1