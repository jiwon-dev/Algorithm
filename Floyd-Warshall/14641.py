import sys
input=sys.stdin.readline
n,m=map(int,input().split())
INF=float('inf')
alp={}
for i in range(26): alp[chr(ord('a')+i)]=i
D=[[INF]*26 for _ in range(26)]
for _ in range(n):
    a,b=input().split()
    D[alp[a]][alp[b]]=1

for k in range(26):
    D[k][k]=1
    for i in range(26):
        for j in range(26):
            D[i][j]=min(D[i][j],D[i][k]+D[k][j])
            
for _ in range(m):
    u,v=input().split()
    if len(u)!=len(v): print('no')
    elif u==v: print('yes')
    else:
        chk=True
        for i in range(len(u)):
            if D[alp[u[i]]][alp[v[i]]]==INF:
                chk=False
        print('yes' if chk else 'no')
