import sys
input=sys.stdin.readline
# 18m
N=int(input())
W=list(map(int,input().split()))
W.sort()

a,b=0,0
dif=float('inf')
for i in range(N):
    start,last=i+1,N-1
    while start<=last:
        mid=(start+last)//2
        if W[i]+W[mid]<0: start=mid+1
        else: last=mid-1
        if dif>abs(W[i]+W[mid]):
            dif=abs(W[i]+W[mid])
            a,b=W[i],W[mid]
print(a+b)
    
