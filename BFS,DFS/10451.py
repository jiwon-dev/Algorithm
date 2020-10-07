import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline
# 06m 09s
# 1부터 n까지 방문하지 않은 곳에 dfs를 돌린다
# dfs의 실행 횟수가 정답이다
def dfs(s):
    if not visited[graph[s]]:
        visited[graph[s]]=1
        dfs(graph[s])

for _ in range(int(input())):
    n=int(input())
    graph=[0]+list(map(int,input().split()))
    visited=[0]*(n+1)
    ans=0
    for i in range(1,n+1):
        if not visited[i]:
            ans+=1
            dfs(i)
    print(ans)
            
            
