import sys
input=sys.stdin.readline
INF=float('inf')
N=int(input())
F=[list(map(int,input().split())) for _ in range(N)]
D=[[INF]*N for _ in range(N)]
for i in range(N):
    for j in range(i+1,N):
        if F[i][0]>F[j][1] or F[j][0]>F[i][1]: continue
        D[i][j]=1;D[j][i]=1

for k in range(N):
    for i in range(N):
        for j in range(N):
            D[i][j]=min(D[i][j],D[i][k]+D[k][j])

for _ in range(int(input())):
    a,b=map(int,input().split())
    print(-1 if D[a-1][b-1]==INF else D[a-1][b-1])
