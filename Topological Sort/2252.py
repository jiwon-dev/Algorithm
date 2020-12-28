import sys
from heapq import *
input=sys.stdin.readline
N,M=map(int,input().split())
H=[[] for _ in range(N+1)]
ind=[0]*(N+1)

for _ in range(M):
    a,b=map(int,input().split())
    ind[b]+=1
    H[a].append(b)

q=[]
for i in range(1,N+1):
    if ind[i]==0: heappush(q,i)

ans=[]
while q:
    u=heappop(q)
    ans.append(u)
    for v in H[u]:
        ind[v]-=1
        if ind[v]==0:
            heappush(q,v)
print(*ans)
