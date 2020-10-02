import sys
from collections import deque
input=sys.stdin.readline
def bfs(r,c):
    q=deque([[r,c]])
    visit[r][c]=1
    while q:
        a,b=q.popleft()
        for k in range(4):
            aa,bb=a+dx[k],b+dy[k]
            if aa<0 or aa==m or bb<0 or bb==n:
                continue
            if not visit[aa][bb]:
                visit[aa][bb]=1
                q.append([aa,bb])
for _ in range(int(input())):
    m,n,k=map(int,input().split())
    dx,dy=[-1,1,0,0],[0,0,-1,1]
    visit,ans=[[1]*n for _ in range(m)],0
    for _ in range(k):
        a,b=map(int,input().split())
        visit[a][b]=0
    for i in range(m):
        for j in range(n):
            if visit[i][j]==0:
                bfs(i,j)
                ans+=1
    print(ans)
