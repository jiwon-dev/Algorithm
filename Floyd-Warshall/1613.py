import sys
input=sys.stdin.readline
# 16m 34s
INF=float('inf')
n,k=map(int,input().split())
D=[[INF]*(n+1) for _ in range(n+1)]
for _ in range(k):
    a,b=map(int,input().split())
    D[a][b]=1;D[b][a]=0
    # a가 b보다 먼저 일어났으면 1, 아니면 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if D[i][k]!=INF and D[i][k]==D[k][j]:
                # i>k and k>j -> i>j(1), i<k and k<j -> i<j(0)
                D[i][j]=D[i][k]

for _ in range(int(input())):
    a,b=map(int,input().split())
    if D[a][b]==1: print(-1)
    elif D[a][b]==0: print(1)
    else: print(0)
                
