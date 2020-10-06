import sys
from collections import deque
input=sys.stdin.readline
# 08m 32s
# bfs(x좌표,y좌표,'W' or 'B')
# bfs는 'W'를 입력받으면 방문하지 않은 것 중 'W'인것만 q에 넣음, 'B'도 마찬가지
# bfs 실행 횟수가 정답
# 단, 혼자 고립되어 있을 경우 count는 0인데 1을 리턴해줘야하니 1 리턴
n,m=map(int,input().split())
MAP=[list(map(str,input().rstrip())) for _ in range(m)]
visited=[[0]*(n+1) for _ in range(m)]
dx,dy=[-1,1,0,0],[0,0,-1,1]
def bfs(x,y,c):
    q=deque([[x,y]])
    count=0
    while q:
        a,b=q.popleft()
        for i in range(4):
            aa,bb=a+dx[i],b+dy[i]
            if 0<=aa<m and 0<=bb<n and not visited[aa][bb] and MAP[aa][bb]==c:
                visited[aa][bb]=1
                q.append([aa,bb])
                count+=1
    if not count:
        return 1
    else:
        return count**2

w=b=0
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            if MAP[i][j]=='W':
                w+=bfs(i,j,'W')
            else:
                b+=bfs(i,j,'B')
print(w,b)
