import sys
from collections import deque
input=sys.stdin.readline
N,M=map(int,input().split())
PD=[list(map(int,input().split())) for _ in range(M)]

indegree=[0]*(N+1)
seq=[[] for _ in range(N+1)]
for i in range(M):
    prev=PD[i][1]
    for j in range(2,PD[i][0]+1):
        cur=PD[i][j]
        indegree[cur]+=1
        seq[prev].append(cur)
        prev=cur

q=deque()
for i in range(1,N+1):
    if indegree[i]==0:
        q.append(i)
    
ans=[]
while q:
    u=q.popleft()
    ans.append(u)
    for v in seq[u]:
        indegree[v]-=1
        if indegree[v]==0:
            q.append(v)
if len(ans)<N: print(0)
else: print(*ans,sep='\n')

