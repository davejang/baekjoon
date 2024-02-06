import sys

INF = int(1e9)

input = sys.stdin.readline
result = 0

def find_parent(x):
  if parent[x] != x:
    parent[x] = find_parent(parent[x])
  return parent[x]

def union(a,b):
  a = find_parent(a)
  b = find_parent(b)

  if a < b:
    parent[b] = a
  else:
    parent[a] = b

n, m = map(int,input().split())
parent = [i for i in range(n+1)]

true_members = list(map(int,input().rstrip().split()))
true_members = true_members[1:]

for member in true_members:
  parent[member] = 0

partys = []

for i in range(m):
  party_members = list(map(int,input().rstrip().split()))
  party_members = party_members[1:]
  partys.append(party_members)

  for i in range(len(party_members)-1):
    union(party_members[i],party_members[i+1])

for party in partys:
  for i in party:
    if find_parent(parent[i]) == 0:
        break
  else:
    result += 1

print(result)