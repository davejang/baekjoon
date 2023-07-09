import sys

input = sys.stdin.readline

n, m = map(int, input().split())
dict = {}

for i in range(n):

    word = input().rstrip()

    if len(word) < m:
        continue
    if word not in dict:
        dict[word] = 1
    else:
        dict[word] += 1

my_list = list(dict.items())
my_list.sort(key = lambda x : (-x[1], -len(x[0]), x[0]))

for i in my_list:
  print(i[0])