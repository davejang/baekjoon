import sys

input = sys.stdin.readline
dict = {}

n, m = map(int,input().split())

for i in range(n):
  word = input().rstrip()
  dict[word] = 1
keywords = set(dict.keys())

length = len(dict)
  
for j in range(m):
  keyword = input().rstrip()
  word_list = keyword.split(',')
  
  in_keyword = set(word_list).intersection(keywords)
  
  if in_keyword:
    for w in in_keyword:
      if dict[w] == 1:
        length -= 1
        dict[w] = 0

  print(length)