import sys
from collections import deque
# 21m 24s
# 연결요소는 노드들이 연결되있는 것인데 간선없이 노드만 있어도 연결요소로 친다
# 따라서, 1~n까지 graph[i]가 없으면(연결된 간선이 없으면) ans+=1 -> 노드만 있는 경우
# graph[i]가 있고 아직 방문하지 않았으면 연결요소가 될 수 있으므로 bfs 실행 후 ans+=1 -> 하나의 연결요소로 되는 경우
# graph[i]가 있는데 방문했으면 이미 하나의 연결요소가 된것이므로 카운트 하면 안됨
input=sys.stdin.readline
n,m=map(int,input().split())
g=[list(map(int,input().split())) for _ in range(m)]
graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)
for a,b in g:
    graph[a].append(b)
    graph[b].append(a)
def bfs(s):
    q=deque([s])
    visited[s]=1
    while q:
        u=q.popleft()
        for v in graph[u]:
            if not visited[v]:
                visited[v]=1
                q.append(v)       
ans=0
for i in range(1,n+1):
    if graph[i]:
        if not visited[i]:
            bfs(i)
            ans+=1
    else:
        ans+=1
print(ans)
