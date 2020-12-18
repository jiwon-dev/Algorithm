import sys
input=sys.stdin.readline
n,m=map(int,input().split())
INF=float('inf')
D=[[INF]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    D[a][b]=1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            D[i][j]=min(D[i][j],D[i][k]+D[k][j])

for _ in range(int(input())):
    a,b=map(int,input().split())
    if D[a][b]!=INF: print(-1)
    elif D[b][a]!=INF: print(1)
    else: print(0)
