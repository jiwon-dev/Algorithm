N,M=int(input()),int(input())
INF=float('inf')
D=[[INF]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a,b=map(int,input().split())
    D[a][b]=1
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            D[i][j]=min(D[i][j],D[i][k]+D[k][j])
for i in range(1,N+1):
    ans=0
    for j in range(1,N+1):
        if i!=j and D[i][j]==INF and D[j][i]==INF: ans+=1
    print(ans)
