import sys
from collections import deque
sys.setrecursionlimit(10**9)
input=sys.stdin.readline
# 19m 00s
# dfs(노드, 깊이)를 0~N 노드까지 다 돌려서 깊이가 4이면 1 출력 후 종료
# 24행의 visited[v]=0을 안해주면 5 5/0 1/1 3/1 2/2 3/3 4 와 같은 입력이 들어왔을 때 반례가 생김
# 따라서 24행의 visited[v]=0을 해줘야함
n,m=map(int,input().split())
graph=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(u,depth):
    if depth==4:
        print(1)
        sys.exit()
    visited[u]=1
    for v in graph[u]:
        if not visited[v]:
            visited[v]=1
            dfs(v,depth+1)
            visited[v]=0

for i in range(n):
    visited=[0]*n
    dfs(i,0)
print(0)


