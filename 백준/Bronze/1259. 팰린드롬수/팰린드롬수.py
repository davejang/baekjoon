result = []
while True:
  word = str(input())
  if word == '0':
    break
  if len(word) == 1:
    result.append('yes')
  else:
    for i in range(len(word)):
      if i+1 == int(len(word) / 2) + 1:
        result.append('yes')
        break
      if word[i] != word[len(word) - i - 1]:
        result.append('no')
        break
for i in result:
  print(i)