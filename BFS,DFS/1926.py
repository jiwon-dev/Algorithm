import sys
from collections import deque
input=sys.stdin.readline
# 07m 54s
# 그림의 개수:bfs 호출 횟수, 가장 넓은 그림의 넓이:bfs를 호출 했을 때 나오는 정사각형의 넓이 중 최댓값
# bfs 호출 조건:not visited[i][j] and MAP[i][j]==1 -> visited[i][j]==1은 이미 하나의 정사각형의 넓이를 구했다는 의미이다
n,m=map(int,input().split())
MAP=[list(map(int,input().split())) for _ in range(n)]
visited=[[0]*m for _ in range(n)]
dx,dy=[-1,1,0,0],[0,0,-1,1]
def bfs(x,y):
    q=deque([[x,y]])
    count=0
    while q:
        a,b=q.popleft()
        visited[a][b]=1
        # count 변수를 쓸거면 제일 처음에 받은 값은 visited를 1로 바꿔야한다
        # 바꾸지 않으면 count가 원하는 값보다 1 크게 된다
        count+=1
        for i in range(4):
            aa,bb=a+dx[i],b+dy[i]
            if 0<=aa<n and 0<=bb<m and MAP[aa][bb] and not visited[aa][bb]:
                q.append([aa,bb])
                visited[aa][bb]=1
    return count

max_value,ans=0,0
for i in range(n):
    for j in range(m):
        if MAP[i][j] and not visited[i][j]:
            ans+=1
            max_value=max(max_value,bfs(i,j))
print(ans)
print(max_value)
