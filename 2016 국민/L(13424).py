import sys
input=sys.stdin.readline
INF=float('inf')
# 1h 10m (1)
for _ in range(int(input())):
    N,M=map(int,input().split())
    D=[[INF]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        a,b,c=map(int,input().split())
        D[a][b]=c;D[b][a]=c

    for k in range(1,N+1):
        D[k][k]=0
        for i in range(1,N+1):
            for j in range(1,N+1):
                D[i][j]=min(D[i][j],D[i][k]+D[k][j])
                
    K=int(input())
    P=list(map(int,input().split()))
    ans=(INF,INF)
    for i in range(1,N+1):
        tmp=0
        for j in range(K):
            tmp+=D[P[j]][i]
        ans=min(ans,(tmp,i))
    print(ans[1])
