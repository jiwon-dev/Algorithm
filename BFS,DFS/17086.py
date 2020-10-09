import sys
from collections import deque
input=sys.stdin.readline
# 18m 43s
# bfs 이용
# 아기 상어가 없는 칸에서 bfs 실행해서 아기상어를 만나면 count 리턴
n,m=map(int,input().split())
MAP=[list(map(int,input().split())) for _ in range(n)]
dx,dy=[-1,1,0,0,-1,-1,1,1],[0,0,-1,1,-1,1,-1,1]

def bfs(x,y):
    q=deque([[x,y]])
    count=0
    visited=[[0]*m for _ in range(n)]
    while q:
        count+=1
        for _ in range(len(q)):
            a,b=q.popleft()
            for i in range(8):
                aa,bb=a+dx[i],b+dy[i]
                if 0<=aa<n and 0<=bb<m and not visited[aa][bb]:
                    if MAP[aa][bb]:
                        return count
                    else:
                        q.append([aa,bb])
                        visited[aa][bb]=1

ans=0
for i in range(n):
    for j in range(m):
        if not MAP[i][j]:
            ans=max(ans,bfs(i,j))
print(ans)
