import sys
input=sys.stdin.readline
n,m,l=map(int,input().split())
h=sorted(map(int,input().split()))
dif=[]
for i in range(1,n):
    dif.append(h[i]-h[i-1])
print(dif)
start,last,ans=0,10**9,0
while start<=last:
    mid=(start+last)//2
    cnt=0
    for v in dif:
        if v>mid:
            cnt+=v//mid
        if v%mid==0:
            cnt-=1
    if cnt>=m:
        start=mid+1
    else:
        last=mid-1
    print(start,last,mid)
