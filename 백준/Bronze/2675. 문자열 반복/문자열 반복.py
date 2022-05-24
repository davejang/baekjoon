n = int(input())
result_list = []

for i in range(n):
  result = ""
  r, word = input().split()
  for j in range(len(word)):
    for k in range(int(r)):
      result = result + word[j] 
  result_list.append(result)
for i in range(n):
  print(result_list[i])