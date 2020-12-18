import sys
input=sys.stdin.readline
# 06m 44s
INF=float('inf')
N,E=map(int,input().split())
D=[[INF]*(N+1) for _ in range(N+1)]
# D[i][i]까지 INF로 한 다음 플로이드 돌린 후, D[출발지][출발지] 중 최솟값이 정답
for _ in range(E):
    a,b,c=map(int,input().split())
    D[a][b]=c
    # 단방향
    
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            D[i][j]=min(D[i][j],D[i][k]+D[k][j])
            
ans=INF
for i in range(1,N+1):
    # ans=min(ans,D[i][i])
    for j in range(1,N+1):
       ans=min(ans,D[i][j]+D[j][i])
       # D[i][j]+D[j][i]:i에서 j까지 갔다가 j에서 i까지 돌아오는 비용
print(-1 if ans==INF else ans)
    
