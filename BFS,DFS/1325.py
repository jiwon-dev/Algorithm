import sys
from collections import deque
# 시간 제한이 빡빡한 문제
# graph[i]가 존재할 때만 bfs 돌림
input=sys.stdin.readline
n,m=map(int,input().split())
result=[]
graph=[[] for _ in range(n+1)]
def bfs(node,count):
    q=deque([node])
    visit=[0]*(n+1)
    visit[node]=1
    while q:
        s=q.popleft()
        count+=1
        for v in graph[s]:
            if not visit[v]:
                q.append(v)
                visit[v]=1
    return count
for _ in range(m):
    a,b=map(int,input().split())
    graph[b].append(a)
for i in range(1,n+1):
    if graph[i]:
        result.append([bfs(i,1),i])
max_value=max(result)[0]
for i in range(len(result)):
    if max_value==result[i][0]:
        print(result[i][1],end=' ')
