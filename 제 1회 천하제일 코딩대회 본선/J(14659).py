import sys
input=sys.stdin.readline
# 31m
N=int(input())
B=list(map(int,input().split()))

ans,cnt,mv=0,0,B[0]
for i in range(1,N):
    if mv<B[i]:
        mv=B[i]
        cnt=0
    else: cnt+=1
    ans=max(ans,cnt)
print(ans)
