import sys
input=sys.stdin.readline
# 21m 58s
# 플로이드 와샬은 dp 방식과 유사
INF=float('inf')
n,m=map(int,input().split())
D=[[INF]*(n+1) for _ in range(n+1)]
# D[i][j]:D[i][j]까지 가는데 양방향 통행으로 바꿔야 할 도로의 최소 개수
for _ in range(m):
    u,v,b=map(int,input().split())
    D[u][v]=0
    D[v][u]=0
    # 입력으로 양방향 도로가 주어지면 바꿔야 할 필요가 없으니 0 입력
    if b==0: D[v][u]=1
    # u->v인 단방향 도로가 주어지면 양방향 도로로 바꿔서 [v][u]에 1 저장
    
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            D[i][j]=min(D[i][j],D[i][k]+D[k][j])
                
for _ in range(int(input())):
    s,e=map(int,input().split())
    if s==e: print(0)
    else: print(D[s][e])
