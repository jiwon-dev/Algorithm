import sys
input=sys.stdin.readline
INF=float('inf')
N,M=map(int,input().split())
V=[int(input()) for _ in range(M)]
D=[list(map(int,input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            D[i][j]=min(D[i][j],D[i][k]+D[k][j])

ans=0
for i in range(M-1): ans+=D[V[i]-1][V[i+1]-1]
print(ans)
