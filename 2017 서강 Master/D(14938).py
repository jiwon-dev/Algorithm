import sys
input=sys.stdin.readline
# 16m
INF=float('inf')
n,m,r=map(int,input().split())
item=list(map(int,input().split()))
D=[[INF]*(n+1) for _ in range(n+1)]
for _ in range(r):
    a,b,c=map(int,input().split())
    D[a][b]=c;D[b][a]=c

for k in range(1,n+1):
    D[k][k]=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            D[i][j]=min(D[i][j],D[i][k]+D[k][j])

ans=0
for i in range(1,n+1):
    tmp=0
    for j in range(1,n+1):
        if D[i][j]<=m: tmp+=item[j-1]
    ans=max(ans,tmp)
print(ans)
