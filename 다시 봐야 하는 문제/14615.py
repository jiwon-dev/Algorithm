import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline
# 1시간 이상
# 원리:정방향, 역방향 graph를 만들어 1->폭탄 있는 곳까지 DFS 수행, N->폭탄 있는 곳까지 DFS 수행해서 총 2번의 DFS로 정답 도출 가능
N,M=map(int,input().split())
graph=[[[] for _ in range(N+1)] for _ in range(2)]

for _ in range(M):
    a,b=map(int,input().split())
    graph[0][a].append(b)
    graph[1][b].append(a)

# 0이 정방향, 1이 역방향
def dfs(x,idx):
    vis[idx][x]=1
    for v in graph[idx][x]:
        if not vis[idx][v]:
            dfs(v,idx)
                
vis=[[0]*(N+1) for _ in range(2)]
dfs(1,0)
# 1에서 끝까지
# N에서 1까지 
dfs(N,1)    
for _ in range(int(input())):
    i=int(input())
    if vis[0][i] and vis[1][i]:
        print('Defend the CTP')
    else:
        print('Destroyed the CTP')


