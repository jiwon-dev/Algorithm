import sys
input=sys.stdin.readline
# 03m 08s
N=int(input())
A,B=map(int,input().split())
C=int(input())
D=sorted([int(input()) for _ in range(N)],reverse=True)
ans=0

for i in range(N+1):
    ans=max(ans,(C+sum(D[:i]))/(A+B*i))
print("%d"%ans)
