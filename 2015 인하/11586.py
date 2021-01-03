import sys
input=sys.stdin.readline
# 01h 38m
N=int(input())
M=[input().rstrip() for _ in range(N)]
K=int(input())

if K==1:
    for i in range(N):
        print(*M[i],sep='')
elif K==2:
    for i in range(N):
        for j in range(N-1,-1,-1):
            print(M[i][j],end='')
        print()
else:
    for i in range(N-1,-1,-1):
        for j in range(N):
            print(M[i][j],end='')
        print()
