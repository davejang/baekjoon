from collections import defaultdict

def solution(gems):
    answer = [1,len(gems)]
    gem_set = set(gems)
    dict = defaultdict(int)
    left = 0
    right = 0
    dict[gems[0]] = 1
    
    while left <= right and right < len(gems):
        if len(dict) < len(gem_set):
            right += 1
            if right >= len(gems):
                break
            dict[gems[right]] += 1
        else:
            if answer[1] - answer[0] > right - left:
                answer = [left+1,right+1]
            dict[gems[left]] -= 1
            if dict[gems[left]] == 0:
                del dict[gems[left]]

            left += 1
    
    return answer