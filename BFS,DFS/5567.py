import sys
from collections import deque
input=sys.stdin.readline
# 19m 08s
# bfs 이용
n=int(input())
m=int(input())
graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)
for _ in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
    # 양방향 그래프

q=deque([1])
# 1에서 시작
visited[1]=1
# 1은 방문했으니 visited[1]=1
count=f=0
# count는 bfs(트리) 깊이, f는 친구(노드) 수
while q:
    count+=1
    # 다음 높이의 트리에 접근하므로 count+=1
    for i in range(len(q)):
        # 다음 노드의 개수가 하나가 아닐 수 있으므로 q에 있는거 모두 빼냄
        u=q.popleft()
        for v in graph[u]:
            if not visited[v]:
                # 방문하지 않았다면 친구로 인정되므로 f+=1
                f+=1
                visited[v]=1
                q.append(v)
    if count==2:print(f);break
    # 레벨 0부터 2까지의 친구만 인정되므로 레벨 2까지 bfs했으면 친구(노드) 수 출력하고 탈출
