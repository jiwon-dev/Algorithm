import sys
from collections import deque
input=sys.stdin.readline
# 11m 14s
N=int(input())
T=[0]*(N+1)
ind=[0]*(N+1)
B=[[] for _ in range(N+1)]

for i in range(1,N+1):
    t,*w=list(map(int,input().split()))
    T[i]=t
    for j in range(1,w[0]+1):
        ind[i]+=1
        B[w[j]].append(i)

q=deque()
ans=[0]*(N+1)
for i in range(1,N+1):
    if ind[i]==0:
        q.append(i)
        ans[i]=T[i]

while q:
    u=q.popleft()
    for v in B[u]:
        ind[v]-=1
        if ind[v]==0: q.append(v)
        ans[v]=max(ans[v],ans[u]+T[v])
print(max(ans))
