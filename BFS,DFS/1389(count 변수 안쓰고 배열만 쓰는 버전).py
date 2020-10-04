import sys
input=sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**9)
n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]

def bfs(i,visited):
    q=deque([i])
    while q:
        for i in range(len(q)):
            s=q.popleft()
            for v in graph[s]:
                if visited[v]==-1:
                    visited[v]=visited[s]+1
                    q.append(v)
            
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
min_value,ans=10**9,0
for i in range(1,n+1):
    total=0
    for j in range(1,n+1):
        visited=[-1]*(n+1)
        visited[i]=0
        bfs(i,visited)
        total+=visited[j]
    if min_value>total:
        min_value=total
        ans=i
print(ans)
    
            
        
