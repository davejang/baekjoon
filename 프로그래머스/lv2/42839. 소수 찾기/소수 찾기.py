from itertools import permutations
import math

def solution(numbers):
    answer = 0
    number_list = []
    numbers = list(numbers)

    for i in range(1,len(numbers)+1):
        p = set(list(permutations(numbers,i)))
        p = [''.join(c) for c in p]
        p = list(map(int,p))
        number_list += p
        
    number_list = list(set(number_list))
        
    for n in number_list:                            
        if n < 2:                                 
            continue
        check = True            
        for i in range(2,int(n**0.5) + 1):        
            if n % i == 0:                        
                check = False
                break
        if check:
            answer += 1

    return answer
