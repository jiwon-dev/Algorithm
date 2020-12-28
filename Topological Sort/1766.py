import sys
from collections import deque
input=sys.stdin.readline
N,M=map(int,input().split())
ind=[0]*(N+1)
D=[[] for _ in range(N+1)]

for _ in range(M):
    a,b=map(int,input().split())
    ind[b]+=1
    D[a].append(b)

q=deque()
for i in range(1,N+1):
    if ind[i]==0: q.append(i)

ans=[]
while q:
    u=q.popleft()
    ans.append(u)
    for v in D[u]:
        ind[v]-=1
        if ind[v]==0:
            q.append(v)
print(*ans)
