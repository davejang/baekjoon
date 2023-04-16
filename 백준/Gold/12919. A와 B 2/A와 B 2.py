word = str(input())
target = str(input())
answer = 0

def calculation(word,target):
  global answer
  if answer == 1:
    return 0
  
  if word == target:
    answer = 1
    return 1
  if len(word) > len(target):
    return 0

  if target[-1] == 'A':
    calculation(word,target[:len(target)-1])
  if target[0] == 'B':
    calculation(word,(target[1:])[::-1])

calculation(word,target)

print(answer)