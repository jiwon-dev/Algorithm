import sys
from collections import deque
# 13m (2)
input=sys.stdin.readline
N,M=map(int,input().split())
W=list(map(int,input().split()))

res=set()
for i in range(M):
    res.add(W[i])
    for j in range(i+1,M):
        res.add(W[i]+W[j])


q=deque()
q.append(0)
dist=[-1]*(N+1)
dist[0]=0

while q:
    u=q.popleft()
    for w in res:
        if u+w>N: continue
        if dist[u+w]!=-1: continue
        dist[u+w]=dist[u]+1
        q.append(u+w)
print(dist[N])
