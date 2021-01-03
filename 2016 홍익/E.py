import sys
input=sys.stdin.readline
# 14m
N,K=map(int,input().split())
M=[int(input()) for _ in range(N)]
start,last=0,2**31
while start<=last:
    mid=(start+last)//2
    temp=0
    for v in M: temp+=v//mid
    if temp>=K: start=mid+1
    else: last=mid-1
print(last)
        
