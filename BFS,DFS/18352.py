import sys
from collections import deque
input=sys.stdin.readline
# 11m 12s
# 스타트가 정해져 있어서 bfs 함수를 만들지 않아도 됨
# 최단 거리는 bfs 돌렸을 때 visit에 들어 있음
n,m,k,x=map(int,input().split())
graph=[[] for _ in range(n+1)]
result=[]
visit=[-1]*(n+1)
visit[x]=0

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)

q=deque([x])
while q:
    s=q.popleft()
    for v in graph[s]:
        if visit[v]==-1:
            visit[v]=visit[s]+1
            q.append(v)

for i in range(1,n+1):
    if visit[i]==k:
        result.append(i)

if not result:
    print(-1)
else:
    print(*result,sep='\n')

