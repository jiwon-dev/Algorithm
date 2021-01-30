import sys
input=sys.stdin.readline
# 19m (1)
name=['PROBRAIN','GROW','ARGOS','ADMIN','ANT','MOTION','SPG','COMON','ALMIGHTY']
N=int(input())
D=[max(list(map(int,input().split()))) for _ in range(9)]
print(name[D.index(max(D))])
