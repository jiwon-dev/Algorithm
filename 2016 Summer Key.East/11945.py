import sys
input=sys.stdin.readline
# 06m
N,M=map(int,input().split())
B=[input().rstrip() for _ in range(N)]
for i in range(N):
    for j in range(M-1,-1,-1):
        print(B[i][j],end='')
    print()
