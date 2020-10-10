import sys
from collections import deque
input=sys.stdin.readline
# 53m 13s
# bfs인데 처음에 익은 토마토들의 좌표를 queues에 넣고 익은 토마토가 다 영향을 줄 때까지 bfs 함수내에서 수행
n,m=map(int,input().split())
queues=deque()
MAP=[]
count=0
for i in range(m):
    row=list(map(int,input().split()))
    for j in range(n):
        if row[j]==1:queues.append((i,j))
        # 익은 토마토들의 좌표를 queues에 넣음
        elif row[j]==-1:count+=1
        # count는 처음에 모든 토마토들이 다 익었을 때를 확인하기 위한 변수(비었을 때의 개수)
    MAP.append(row)
first=len(queues)
# first는 퍼지기 전에 익은 토마토들의 개수이고 count+first가 n*m이면 퍼지기 전에 다 익은 토마토들만 입력을 받은 것임을 체크
dx,dy=[-1,1,0,0],[0,0,-1,1]

def cal():
    # bfs 다 돌렸을 때 안 익은 토마토가 있는지 확인하는 함수
    for i in range(m):
        for j in range(n):
            if not MAP[i][j]:
                return True
    return False

def bfs(q):
    time=-1
    while q:
        time+=1
        for _ in range(len(q)):
            a,b=q.popleft()
            for i in range(4):
                aa,bb=a+dx[i],b+dy[i]
                if 0<=aa<m and 0<=bb<n and not MAP[aa][bb]:
                    # 안 익은 토마토들만 MAP에 익었다고 표시하고 q에 넣음
                    MAP[aa][bb]=1
                    q.append((aa,bb))
    return time

ans=bfs(queues)
if first+count==n*m:print(0)
elif cal():print(-1)
else:print(ans)
