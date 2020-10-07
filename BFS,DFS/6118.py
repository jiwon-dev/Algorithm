import sys
from collections import deque
input=sys.stdin.readline
# 09m 01s
# bfs와 disc 배열을 이용해 해결
# disc는 방문하지 않았으면 -1, 방문했으면 최소 거리를 저장
n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

disc=[-1]*(n+1)
disc[1]=0
q=deque([1])
while q:
    u=q.popleft()
    for v in graph[u]:
        if disc[v]==-1:
            disc[v]=disc[u]+1
            q.append(v)

max_value=max(disc)
print(disc.index(max_value),max_value,disc.count(max_value))
