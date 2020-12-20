import sys
input=sys.stdin.readline
# 12m 13s
INF=float('inf')
for _ in range(int(input())):
    N=int(input())
    V=list(map(int,input().split()))
    D=[list(map(int,input().split())) for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if D[i][j]==-1: D[i][j]=INF

    for k in range(N):
        for i in range(N):
            for j in range(N):
                D[i][j]=min(D[i][j],D[i][k]+D[k][j])

    ans=0
    for i in range(N-1): ans+=D[V[i]][V[i+1]]
    ans+=D[V[-1]][V[0]]
    # 여행을 다 갔다온 뒤, 처음으로 돌아오는 것까지 계산
    print('impossible' if ans==INF else ans)
