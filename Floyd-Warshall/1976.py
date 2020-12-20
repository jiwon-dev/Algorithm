import sys
input=sys.stdin.readline
INF=float('inf')
N,M=int(input()),int(input())
D=[list(map(int,input().split())) for _ in range(N)]
for i in range(N):
    D[i][i]=1
    # 시작점에서 시작점으로 가는 경우도 여행 가능
    for j in range(N):
        if not D[i][j]: D[i][j]=INF

for k in range(N):
    for i in range(N):
        for j in range(N):
            D[i][j]=min(D[i][j],D[i][k]+D[k][j])

V=list(map(int,input().split()))
ans=True
for i in range(M-1):
    if D[V[i]-1][V[i+1]-1]==INF:
        # 여행 가능한 경로가 한 번이라도 없다면 False
        ans=False
        break
print('YES' if ans else 'NO')
