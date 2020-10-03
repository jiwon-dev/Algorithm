import sys
from collections import deque
input=sys.stdin.readline
# 22m 10s
# bfs(양,늑대,x좌표,y좌표) -> dx,dy를 이용해 상하좌우를 살피며 아직 방문하지 않았고 'v'이면 w+=1,'o'이면 s+=1 후, 방문했으니
# visited[aa][bb]=1로 바꾸고 deque에 넣음
# dfs는 stk을 이용해 꺼낸 뒤 'v'이면 w+=1, 'o'이면 s+=1
r,c=map(int,input().split())
dx,dy=[-1,1,0,0],[0,0,-1,1]
MAP=[input().rstrip() for _ in range(r)]
visited=[[0]*c for _ in range(r)]
def dfs(x,y):
    stk=[[x,y]]
    visited[x][y]=1
    s=w=0
    while stk:
        a,b=stk.pop()
        # stk에서 좌표하나 꺼내고 'v'이면 w+=1,'o'이면 s+=1
        if MAP[a][b]=='v':w+=1
        elif MAP[a][b]=='o':s+=1
        for i in range(4):
            aa,bb=a+dx[i],b+dy[i]
            # 꺼낸 좌표의 상하좌우 살핌
            if 0<=aa<r and 0<=bb<c:
                # 인덱스 에러 처리
                if MAP[aa][bb]=='#' or visited[aa][bb]:continue
                # 상하좌우 살폈을 때, '#' 이거나 방문했으면 볼 필요 없으므로 continue
                visited[aa][bb]=1
                stk.append([aa,bb])
                # 아니면, 방문 표시하고 stk에 넣음
    if w>=s:s=0
    else:w=0
    return s,w
sheep,wolf=0,0
for i in range(r):
    for j in range(c):
        if visited[i][j]:continue
        # 방문했으면 continue
        if MAP[i][j]=='v' or MAP[i][j]=='o':
            # 늑대나 양이면 dfs 돌림
            x,y=dfs(i,j)
            sheep+=x;wolf+=y
print(sheep,wolf)
