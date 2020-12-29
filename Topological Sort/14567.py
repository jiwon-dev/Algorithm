import sys
from collections import deque
input=sys.stdin.readline
# 05m 54s
N,M=map(int,input().split())
ind=[0]*(N+1)
B=[[] for _ in range(N+1)]

for _ in range(M):
    a,b=map(int,input().split())
    ind[b]+=1
    B[a].append(b)

q=deque()
ans=[1]*(N+1)
for i in range(1,N+1):
    if ind[i]==0: q.append(i)

while q:
    u=q.popleft()
    for v in B[u]:
        ind[v]-=1
        if ind[v]==0:
            q.append(v)
            ans[v]=ans[u]+1
            # 현재 듣는 과목은 이전에 들었던 과목보다 한 학기 뒤에 들으므로 ans[v]=ans[u]+1
print(*ans[1:])
