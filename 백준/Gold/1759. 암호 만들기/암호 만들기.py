from itertools import combinations

L, C = map(int,input().split())
word = list(map(str,input().split()))
word.sort()
password = []
collection_count = 0

for i in combinations(word, L):
  if 'a' in i:
    collection_count = 1
    if 'e' in i:
      collection_count = collection_count + 1
    if 'i' in i:
      collection_count = collection_count + 1
    if 'o' in i:
      collection_count = collection_count + 1
    if 'u' in i:
      collection_count = collection_count + 1
    if(L - collection_count >= 2):
      result = ''.join(i)
      print(result)
  elif 'e' in i:
    collection_count = 1
    if 'i' in i:
      collection_count = collection_count + 1
    if 'o' in i:
      collection_count = collection_count + 1
    if 'u' in i:
      collection_count = collection_count + 1
    if(L - collection_count >= 2):
      result = ''.join(i)
      print(result)
  elif 'i' in i:
    collection_count = 1
    if 'o' in i:
      collection_count = collection_count + 1
    if 'u' in i:
      collection_count = collection_count + 1
    if(L - collection_count >= 2):
      result = ''.join(i)
      print(result)
  elif 'o' in i:
    collection_count = 1
    if 'u' in i:
      collection_count = collection_count + 1
    if(L - collection_count >= 2):
      result = ''.join(i)
      print(result)
  elif 'u' in i:
    collection_count = 1
    if(L - collection_count >= 2):
      result = ''.join(i)
      print(result)