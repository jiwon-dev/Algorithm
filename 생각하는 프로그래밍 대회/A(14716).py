import sys
from collections import deque
input=sys.stdin.readline
# 05m
def bfs(x,y):
    q=deque()
    q.append((x,y))

    while q:
        a,b=q.popleft()
        for aa,bb in (a-1,b),(a+1,b),(a,b-1),(a,b+1),(a-1,b-1),(a-1,b+1),(a+1,b-1),(a+1,b+1):
            if not (0<=aa<M and 0<=bb<N): continue
            if visited[aa][bb]: continue
            if H[aa][bb]==1:
                visited[aa][bb]=1
                q.append((aa,bb))
                
M,N=map(int,input().split())
H=[list(map(int,input().split())) for _ in range(M)]

ans=0
visited=[[False]*N for _ in range(M)]
for i in range(M):
    for j in range(N):
        if not visited[i][j] and H[i][j]:
            visited[i][j]=True
            bfs(i,j)
            ans+=1
print(ans)
