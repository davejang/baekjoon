N = int(input())
dp = []
dp.append(1)
dp.append(2)

if N < 3:
  print(dp[N-1])
else:
  temp = 3
  while True:
    dp.append((dp[temp-2]+dp[temp-3])%15746)
    if temp == N:
      break
    temp +=1
  print(dp[N-1])