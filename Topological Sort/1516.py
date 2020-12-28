import sys
from collections import deque
input=sys.stdin.readline
N=int(input())
B=[[] for _ in range(N+1)]
T=[0]*(N+1)
ind=[0]*(N+1)

for i in range(1,N+1):
    row=list(map(int,input().split()))
    T[i]=row[0]
    j=1
    while True:
        if row[j]==-1: break
        ind[i]+=1
        B[row[j]].append(i)
        j+=1

q=deque()
for i in range(1,N+1):
    if ind[i]==0: q.append(i)

ans=[0]*(N+1)
while q:
    u=q.popleft()
    ans[u]+=T[u]
    for v in B[u]:
        ind[v]-=1
        if ind[v]==0:
            ans[v]+=ans[u]
            q.append(v)
print(*ans[1:],sep='\n')
            
