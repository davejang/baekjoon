import sys
input = sys.stdin.readline
password = {}
n, m = map(int,input().split())
for i in range(n):
  site, pw = input().rstrip().split()
  password[site] = pw
for i in range(m):
  site = input().rstrip()
  print(password[site])