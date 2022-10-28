from itertools import combinations

n = int(input())
dp = []

for i in range(1,11):
  for j in combinations(range(10),i):
    num = sorted(list(j),reverse = True)
    dp.append(int("".join(map(str,num))))

dp.sort()
if n >= len(dp):
  print(-1)
else:
  print(dp[n])