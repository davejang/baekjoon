import sys

input = sys.stdin.readline

n = int(input())
rank = []
result = 0
min_rank = []
for i in range(n):
  rank.append(int(input()))
  min_rank.append(i+1)

rank.sort()
for i in range(n):
  result += abs(rank[i] - min_rank[i])

print(result)