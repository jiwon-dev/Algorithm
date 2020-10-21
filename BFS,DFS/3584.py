import sys
from collections import deque
input=sys.stdin.readline
# 27m 36s
# 어차피 부모노드는 하나이니 graph[자식노드]=[부모노드]로 만들어 놓고 bfs(찾아야하는 노드)을 수행
def bfs(s):
    res=[s]
    visited=[0]*(n+1)
    visited[s]=1
    q=deque()
    q.append(s)
    while q:
        u=q.popleft()
        v=graph[u]
        if v==0:
            return res
        if not visited[v]:
            visited[v]=1
            q.append(v)
            res.append(v)
    return res

for _ in range(int(input())):
    n=int(input())
    graph=[0]*(n+1)
    for _ in range(n-1):
        a,b=map(int,input().split())
        graph[b]=a
    t1,t2=map(int,input().split())
    res1=bfs(t1)
    res2=bfs(t2)
    for i in res1:
        if i in res2:
            print(i)
            break
    
