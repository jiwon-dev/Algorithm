import sys
from collections import deque
input=sys.stdin.readline
# 58m 20s
# 최단 거리이니 bfs 이용
# disc[x좌표][y좌표][i번째 악당]:i번째 악당별로 x좌표,y좌표까지 가는데 걸리는 시간을 재야하므로 3차원 배열로 만듬
# 각 악당의 위치에서 x좌표,y좌표까지 가는데 걸리는 시간을 넣음
# 세 악당의 disc 중 -1이 하나라도 있으면 세 악당 모두 만나지 못하므로 -1을 result에 넣어야하는데
# 시간의 최솟값을 알아야하므로 경계값 999999를 넣음
r,c=map(int,input().split())
grid=[list(map(int,input().rstrip())) for _ in range(r)]
disc=[[[-1 for _ in range(c)] for _ in range(r)] for _ in range(3)]
start=[list(map(int,input().split())) for _ in range(3)]
dx,dy=[-1,1,0,0],[0,0,-1,1]
result=[[-1]*c for _ in range(r)]
dic={}

def bfs(x,y,i):
    q=deque()
    q.append([x,y])
    disc[i][x][y]=0
    while q:
        a,b=q.popleft()
        for j in range(4):
            aa,bb=a+dx[j],b+dy[j]
            if 0<=aa<r and 0<=bb<c and disc[i][aa][bb]==-1 and not grid[aa][bb]:
                disc[i][aa][bb]=disc[i][a][b]+1
                q.append([aa,bb])

for i in range(3):
    bfs(start[i][0]-1,start[i][1]-1,i)

for i in range(r):
    for j in range(c):
        for k in range(3):
            if disc[k][i][j]==-1:result[i][j]=999999
            result[i][j]=max(result[i][j],disc[k][i][j])
        if result[i][j] not in dic:
            dic[result[i][j]]=1
        else:
            dic[result[i][j]]+=1
ans=min(dic.items())
if ans[0]==999999:print(-1)
else:print(*ans,sep='\n')
