import sys
input=sys.stdin.readline
# 05m 43s
N,M=map(int,input().split())
D=[list(map(int,input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            D[i][j]=min(D[i][j],D[i][k]+D[k][j])

for _ in range(M):
    a,b,c=map(int,input().split())
    if D[a-1][b-1]<=c: print('Enjoy other party')
    else: print('Stay here')
