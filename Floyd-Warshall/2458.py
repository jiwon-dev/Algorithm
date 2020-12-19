import sys
input=sys.stdin.readline
INF=float('inf')
N,M=map(int,input().split())
D=[[INF]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a,b=map(int,input().split())
    D[a][b]=1

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            D[i][j]=min(D[i][j],D[i][k]+D[k][j])

ans=0
for i in range(1,N+1):
    total=0
    for j in range(1,N+1):
        if D[i][j]<INF or D[j][i]<INF: total+=1
    if total==N-1: ans+=1
print(ans)
