n = int(input())
result_list = []

for i in range(n):
  quiz = input()
  result = 0
  correct = 0
  for j in range(len(quiz)):
    if j == 0:
      if quiz[j] == 'O':
        result = result + 1
        correct = 1
    else:
      if quiz[j-1] == 'O' and quiz[j] == 'O':
        correct = correct + 1
        result = result + correct
      elif quiz[j] == 'O':
        correct = 1
        result = result + correct
      else:
        correct = 0
  result_list.append(result)

for i in result_list:
  print(i)