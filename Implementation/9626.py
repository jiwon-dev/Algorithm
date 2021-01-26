import sys
input=sys.stdin.readline
M,N=map(int,input().split())
U,L,R,D=map(int,input().split())
C=[input().rstrip() for _ in range(M)]

puz=[['.']*(L+R+N) for _ in range(U+D+M)]
for i in range(0,U+D+M,2):
    for j in range(0,L+R+N,2):
        puz[i][j]='#'
for i in range(1,U+D+M,2):
    for j in range(1,L+R+N,2):
        puz[i][j]='#'

for i in range(U,M+U):
    for j in range(L,N+L):
        puz[i][j]=C[i-U][j-L]

for i in range(U+D+M): print(*puz[i],sep='')

