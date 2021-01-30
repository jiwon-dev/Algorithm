import sys
input=sys.stdin.readline
N=int(input())
R=[int(input()) for _ in range(N)]
mv=min(R)
print(mv*N)
