import sys
input=sys.stdin.readline
# 01h 02m
N=int(input())
C=list(map(int,input().split()))

M=0
ans=0
for v in C:
    if v==M: M=(M+1)%3; ans+=1
print(ans)
