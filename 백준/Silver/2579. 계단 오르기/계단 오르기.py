n = int(input())
score = []
score_sum = [0] * (n + 1)
for i in range(n):
  score.append(int(input())) 
if n >= 3:
  score_sum[0] = score[0]
  score_sum[1] = score[0] + score[1]
  score_sum[2] = max(score[0]+score[2],score[1]+score[2])
  for i in range(3,n):
    score_sum[i] = max(score_sum[i-3]+score[i-1] +score[i],score_sum[i-2]+ score[i])
  print(score_sum[n-1])
elif n == 2:
  print(max(score[0]+score[1],score[1]))
else:
  print(score[0])
