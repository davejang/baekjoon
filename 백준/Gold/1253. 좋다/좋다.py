import sys

n = int(input())
# number_count = {}
answer = 0
number_list = list(map(int,sys.stdin.readline().rstrip().split()))
number_list.sort()

for i in range(n):
    tmp = number_list[:i] + number_list[i+1:]
    left = 0
    right = len(tmp) - 1
    while left < right:
        sum = tmp[left] + tmp[right]
        if sum == number_list[i]:
            answer += 1
            break
        # 합이 클 경우 큰 숫자 감소
        if sum < number_list[i]: 
          left += 1 
        # 합이 작을 경우 작은 숫자 증가
        else: 
          right -= 1 
          
# for i in range(n-1):
#   for j in range(i+1,n):
#     sum = number_sort[i] + number_sort[j]
#     if sum in number_list:
#       number_count[sum] = 1

print(answer)