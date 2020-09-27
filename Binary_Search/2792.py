import sys
input=sys.stdin.readline
# 항상 최대로 나눠준다고 생각하고 이분 탐색
# mid가 최대로 나눠주는 값
n,m=map(int,input().split())
j=[int(input()) for _ in range(m)]
start,last,ans=0,10**9,10**9
while start<=last:
    mid=(start+last)//2
    total=0
    for value in j:
        total+=value//mid
        if value%mid:total+=1
    if total<=n:
        ans=min(ans,mid)
        last=mid-1
    else:
        start=mid+1  
print(ans)
