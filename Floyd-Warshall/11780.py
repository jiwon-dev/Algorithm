import sys
input=sys.stdin.readline
INF=float('inf')
n=int(input())
m=int(input())
D=[[INF]*(n+1) for _ in range(n+1)]
path=[[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    D[a][b]=min(D[a][b],c)
    path[a][b]=a

for k in range(1,n+1):
    D[k][k]=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if D[i][j]>D[i][k]+D[k][j]:
                D[i][j]=D[i][k]+D[k][j]
                path[i][j]=path[k][j]
for i in range(1,n+1):
    for j in range(1,n+1):
        print(D[i][j],end=' ')
    print()
    
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j: print(0)
        else:
            l=path[i][j]
            ans=[j]
            while l!=i:
                ans.append(l)
                l=path[i][l]
            ans.append(i)
            print(len(ans),end=' ')
            print(*ans[::-1])
