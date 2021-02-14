import sys
input=sys.stdin.readline
# 44m
N,K,D=map(int,input().split())
B=[list(map(int,input().split())) for _ in range(K)]
start,last=1,1000000
while start<=last:
    mid=(start+last)//2
    tmp=0
    for a,b,c in B:
        if mid>b: tmp+=(b-a)//c+1; continue
        if mid<a: continue
        tmp+=(mid-a)//c+1
    if tmp>=D: last=mid-1
    else: start=mid+1
print(start)
