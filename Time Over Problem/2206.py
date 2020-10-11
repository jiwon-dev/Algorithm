import sys
from collections import deque
input=sys.stdin.readline
# 1시간 이상
# disc(방문 리스트)를 3차원 배열 [벽 부쉈는지 여부][y 좌표][x 좌표]로 만든다
n,m=map(int,input().split())
grid=[list(map(int,input().rstrip())) for _ in range(n)]
disc=[[[-1 for _ in range(m)] for _ in range(n)] for _ in range(2)]
disc[0][0][0]=1

q=deque([[0,0,0]])
# [x좌표,y좌표,벽 부순 횟수]
while q:
    a,b,c=q.popleft()
    for aa,bb in (a-1,b),(a+1,b),(a,b-1),(a,b+1):
        if 0<=aa<n and 0<=bb<m:
            if not grid[aa][bb] and disc[c][aa][bb]==-1:
                # 이동할 수 있고 아직 방문 하지 않았다면
                disc[c][aa][bb]=disc[c][a][b]+1
                # 방문 표시(거리 더해줌) 후 큐에 추가
                q.append([aa,bb,c])
            if c==0 and grid[aa][bb]==1 and disc[c+1][aa][bb]==-1:
                # 벽을 부술 수 있고 벽을 만났고 벽을 부쉈을 때 방문 하지 않았다면
                disc[c+1][aa][bb]=disc[c][a][b]+1
                # 벽을 부쉈으니 부순 곳에 거리 표시하고 큐에 추가
                q.append([aa,bb,c+1])
ans=min(disc[0][-1][-1],disc[1][-1][-1])
print(max(disc[0][-1][-1],disc[1][-1][-1]) if ans==-1 else ans)
