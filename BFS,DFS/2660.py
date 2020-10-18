import sys
from collections import deque
input=sys.stdin.readline
# 17m 36s
# 1~n까지 bfs(스타트 노드)를 했을 때 깊이 중 최솟값이 회장의 점수
# bfs 종료 조건:모든 노드를 방문했을 때
n=int(input())
graph=[[] for _ in range(n+1)]
result=[]
while True:
    a,b=map(int,input().split())
    if a==-1 and b==-1:
        break
    graph[a].append(b)
    graph[b].append(a)

def bfs(s):
    q=deque([s])
    visited[s]=1
    depth=-1
    while q:
        depth+=1
        for _ in range(len(q)):
            u=q.popleft()
            for v in graph[u]:
                if not visited[v]:
                    visited[v]=1
                    q.append(v)
    return depth

for i in range(1,n+1):
    visited=[0]*(n+1)
    result.append(bfs(i))

min_value=min(result)
print(min_value,result.count(min_value))
for i in range(n):
    if result[i]==min_value:
        print(i+1,end=' ')
