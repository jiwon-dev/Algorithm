import sys
from collections import deque
input=sys.stdin.readline
# 21m 39s
# 처음에 각 텔레포트 정거장 마다 텔레포트가 하나만 있는 줄 알았는데 2개 이상 있을 수도 있었음
# 텔레포트는 양방향으로 탈 수 있으니 양방향 그래프
n,m=map(int,input().split())
s,e=map(int,input().split())
graph=[[]*(n+1) for _ in range(n+1)]
visit=[-1]*(n+1)
visit[s]=0

for _ in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(s):
    q=deque([s])
    while q:
        r=q.popleft()
        for i in [r-1,r+1]:
            if 1<=i<=n and visit[i]==-1:
                visit[i]=visit[r]+1
                q.append(i)
        if graph[r]:
            for v in graph[r]:
                if 1<=v<=n and visit[v]==-1:
                    visit[v]=visit[r]+1
                    q.append(v)
bfs(s)
print(visit[e])
