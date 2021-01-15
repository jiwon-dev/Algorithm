import sys
input=sys.stdin.readline
INF=float('inf')
N,M=map(int,input().split())
H=list(map(int,input().split()))
D=[[INF]*(N+1) for _ in range(N+1)]
for _ in range(M):
    x,y=map(int,input().split())
    D[x][y]=1
    D[y][x]=1

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            D[i][j]=min(D[i][j],D[i][k]+D[k][j])
print(D,H)
for _ in range(int(input())):
    A,K=map(int,input().split())
    mv=INF
    for i in range(1,N+1):
        if D[A][i]==K: mv=min(mv,H[i-1])
    print(mv)
