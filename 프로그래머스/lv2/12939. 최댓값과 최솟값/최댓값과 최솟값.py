def solution(s):
    str_list = list(map(int,s.split(' ')))
    str_list.sort()
    min_num = str_list[0]
    max_num = str_list[-1]
    answer = str(min_num) + " " + str(max_num)
    return answer