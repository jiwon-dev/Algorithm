import sys
from collections import deque
input=sys.stdin.readline
# 05m 43s
# bfs와 count 변수 안쓰고 disc 배열을 써서 해결
sys.setrecursionlimit(10**9)
a,b=map(int,input().split())
n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
disc=[-1]*(n+1)
disc[a]=0

for _ in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

q=deque([a])
while q:
    u=q.popleft()
    for v in graph[u]:
        if disc[v]==-1:
            disc[v]=disc[u]+1
            q.append(v)
print(disc[b])

