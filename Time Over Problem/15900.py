import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline
# 1시간 이상
# 모든 리프노드 까지의 거리를 더했을 때 짝수이면 'No', 홀수이면 'Yes'를 출력하면 된다
# dfs를 재귀로 구현하되 dfs(현재 노드,높이)로 만들어서 dfs 호출할 때마다 높이가 1 늘어나게끔 한다
# 리프노드이면 cnt에 높이를 더한다
n=int(input())
graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)
for _ in range(n-1):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

cnt=0
def dfs(u,h):
    # 한 번이라도 재귀 호출되면 리프노드가 아님
    global cnt
    visited[u]=1
    isLeaf=True
    # 리프노드인지 아닌지 판별하는 변수(True이면 리프노드)
    for v in graph[u]:
        if not visited[v]:
            isLeaf=False
            dfs(v,h+1)
    if isLeaf:cnt+=h
    
dfs(1,0)
print('No' if cnt%2==0 else 'Yes')
