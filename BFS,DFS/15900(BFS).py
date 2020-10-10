import sys
from collections import deque
input=sys.stdin.readline
# bfs 이용
# 리프 노드의 graph[리프 노드]의 개수는 1임을 이용해서 disc로 1부터 각 노드까지의 거리를 구한뒤 len(graph[노드])==1인 것만 더한다
n=int(input())
graph=[[] for _ in range(n+1)]
disc=[-1]*(n+1)
disc[1]=0
for _ in range(n-1):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

q=deque([1])
while q:
    u=q.popleft()
    for v in graph[u]:
        if disc[v]==-1:
            disc[v]=disc[u]+1
            q.append(v)
h=sum(disc[v] for v in range(1,n+1) if len(graph[v])==1)
print('No' if not h%2 else 'Yes')
