import sys
input=sys.stdin.readline
N=range(int(input()))
D=[list(map(int,input().split())) for _ in N]

for k in N:
    for i in N:
        for j in N:
            if D[i][j]: continue
            if D[i][k]+D[k][j]==2: D[i][j]=1

for i in N: print(*D[i])
