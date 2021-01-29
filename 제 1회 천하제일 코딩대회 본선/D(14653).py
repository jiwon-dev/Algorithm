import sys
input=sys.stdin.readline
N,K,Q=map(int,input().split())
M=[input().split() for _ in range(K)][::-1]

res=[chr(ord('A')+i) for i in range(1,N)]
for i in range(K):
    if M[i][1] in res: res.pop(res.index(M[i][1]))
    if K-i==Q:
        if not res or M[i][0]=='0': print(-1)
        else: print(*res)
        break
