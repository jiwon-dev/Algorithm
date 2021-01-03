import sys
import itertools
# 36m
input=sys.stdin.readline
N,M=map(int,input().split())
pick=[i for i in range(M)]
P=[[] for _ in range(M)]

for i in range(M):
    O,*p=input().split()
    P[i]=p

ans=set([str(i) for i in range(1,N+1)])
for i in range(1,M+1):
    temp=itertools.combinations(pick,i)
    for v in temp:
        union=set()
        for j in range(len(v)):
            for k in P[v[j]]:
                union.add(k)
        if union==ans:
            print(len(v))
            sys.exit()
print(-1)
            
