import sys
from collections import deque
input=sys.stdin.readline
# 1시간 이상
n,k=map(int,input().split())
disc=[[-1,0] for _ in range(100002)]
# [거리,방법의 수]

q=deque()
q.append(n)
disc[n][0]=0
disc[n][1]=1
# 시작 지점이니 거리:0,방법의 수:1
while q:
    u=q.popleft()
    for v in (u-1),(u+1),(2*u):
        if 0<=v<=100000:
            if disc[v][0]==-1:
                # 처음 방분했다면
                disc[v][0]=disc[u][0]+1
                # 거리 1 늘려주고
                disc[v][1]=disc[u][1]
                # 방법은 u를 그대로 따라감
                q.append(v)
                # q에 넣음
            elif disc[v][0]==disc[u][0]+1:
                # 처음 방문하지 않았고 u의 방법보다 1 크다면
                disc[v][1]+=disc[u][1]
                # u를 거쳐 v에 가므로 u의 방법을 더해줌
print(*disc[k],sep='\n')
