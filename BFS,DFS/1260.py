import sys
from collections import deque
# 34m 29s
# bfs는 deque 사용, dfs는 재귀
input=sys.stdin.readline
n,m,v=map(int,input().split())
connected=[[] for _ in range(n+1)]
l=[list(map(int,input().split())) for _ in range(m)]
for a,b in l:
    connected[a].append(b)
    connected[b].append(a)
for l in connected:
    l.sort()
def bfs(s):
    visited=[s]
    q=deque([s])
    while q:
        node=q.popleft()
        print(node,end=' ')
        for v in connected[node]:
            if v not in visited:
                visited.append(v)
                q.append(v)
visited=[0]*(n+1)
def dfs(s,visited):
    visited[s]=1
    print(s,end=' ')
    for i in connected[s]:
        if not visited[i]:
            dfs(i,visited)
dfs(v,visited)
print()
bfs(v)

