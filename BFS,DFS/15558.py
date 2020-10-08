import sys
from collections import deque
sys.setrecursionlimit(10**9)
input=sys.stdin.readline
# 40m 18s
# 최단 경로이니 bfs 이용
# 한칸 움직일 때마다 제일 앞쪽 칸들 없어지니 visited[0][count]=1,visited[1][count]=1
n,k=map(int,input().split())
MAP=[list(map(int,input().rstrip())) for _ in range(2)]
visited=[[0]*n for _ in range(2)]
dx,dy=[0,0,1,-1],[-1,1,k,k]
# [좌 ,우 ,왼쪽 줄 ,오른쪽 줄]

q=deque([[0,0]])
visited[0][0]=1
count=-1
# 0부터 없애야하니 처음 값은 -1
while q:
    count+=1
    for i in range(len(q)):
        x,y=q.popleft()
        for j in range(4):
            xx,yy=x+dx[j],y+dy[j]
            if 0<=xx<2 and 0<=yy<n and MAP[xx][yy] and not visited[xx][yy]:
                visited[xx][yy]=1
                q.append([xx,yy])
            if 0<=xx<2 and yy>=n:
                # visited 열의 개수를 n-1까지만 만들어 놓고 bfs했을 때 n이상이면 클리어했으므로 1 출력후 종료
                print(1)
                sys.exit()
        visited[0][count]=1
        visited[1][count]=1
        # 한 칸 움직였으니 제일 앞쪽 칸 이동한걸로 침
print(0)
