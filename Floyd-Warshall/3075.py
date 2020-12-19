import sys
input=sys.stdin.readline
INF=float('inf')
for _ in range(int(input())):
    n,p,q=map(int,input().split())
    P=[int(input()) for _ in range(n)]
    D=[[INF]*101 for _ in range(101)]
    for _ in range(q):
        i,j,d=map(int,input().split())
        D[i][j]=min(D[i][j],d)
        D[j][i]=min(D[j][i],d)

    for k in range(1,p+1):
        D[k][k]=0
        for i in range(1,p+1):
            for j in range(1,p+1):
                D[i][j]=min(D[i][j],D[i][k]+D[k][j])
                
    ans=(INF,INF)
    for i in range(1,p+1):
        total=0
        chk=True
        for v in P:
            if D[v][i]==INF:
                chk=False
                break
            total+=D[v][i]**2
        if chk: ans=min(ans,(total,i))
    print(*ans[::-1])
