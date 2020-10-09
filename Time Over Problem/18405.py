import sys
from collections import deque
input=sys.stdin.readline
# 1시간 이상
# bfs인데 순서가 있으므로 queues에 좌표를 넣어서 1부터 k까지 채워나감
n,k=map(int,input().split())
MAP=[]
queues=[[] for _ in range(k+1)]
dx,dy=[-1,1,0,0],[0,0,-1,1]

for i in range(n):
    row=list(map(int,input().split()))
    for j in range(n):
        if row[j]:
            # row[j]가 0이 아니면 바이러스가 존재하는 경우이므로 queues[row[j]]에 해당 좌표를 추가
            queues[row[j]].append((i,j))
    MAP.append(row)

s,r,c=map(int,input().split())
for time in range(s):
    # 0부터 s의 시간까지 bfs
    for Q in queues:
        # queues에 있는거 1부터 순서대로 바이러스를 퍼트림
        nq=[]
        # 그냥 bfs를 하면 현재좌표에서 상하좌우에 방문했다는 표시가 남으므로 bfs를 못돌리니까
        # nq라는 리스트를 새로 만들어 시간대별로 1~k까지 돌린다음 Q를 nq로 초기화하는 방식으로 사용
        # nq에는 바이러스를 퍼트린 좌표가 들어감
        for i,j in Q:
            for k in range(4):
                ii,jj=i+dx[k],j+dy[k]
                if 0<=ii<n and 0<=jj<n and not MAP[ii][jj]:
                    MAP[ii][jj]=MAP[i][j]
                    nq.append((ii,jj))
        Q[:]=nq
print(MAP[r-1][c-1])
        


