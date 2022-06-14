n, m = map(int,input().split())
not_listend = []
not_seen = []
for i in range(n):
  person = str(input())
  not_listend.append(person)
for i in range(m):
  person = str(input())
  not_seen.append(person)
set1 = set(not_listend)
set2 = set(not_seen)
result = sorted(set1.intersection(set2))
print(len(result))
for i in result:
  print(i)