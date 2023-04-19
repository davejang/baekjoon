import sys

n = int(input())
# number_count = {}
answer = 0
number_list = list(map(int,sys.stdin.readline().rstrip().split()))
number_list.sort()

for i in range(n):
    tmp = number_list[:i] + number_list[i+1:]
    left, right = 0, len(tmp) - 1
    while left < right:
        t = tmp[left] + tmp[right]
        if t == number_list[i]:
            answer += 1
            break
        if t < number_list[i]: left += 1 
        else: 
          right -= 1 
          
# for i in range(n-1):
#   for j in range(i+1,n):
#     sum = number_sort[i] + number_sort[j]
#     if sum in number_list:
#       number_count[sum] = 1

print(answer)
