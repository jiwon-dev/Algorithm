import sys
input=sys.stdin.readline
# 시간을 기준으로 이분탐색하는데 답이 10**9보다 더 클 수도 있어서 10**100으로 두고 시작
# mid가 시간이면 각 데스크 당 받을 수 있는 사람:mid//각 데스크에서의 심사시간
# 각 데스크 당 받을 수 있는 사람의 총 합이 m보다 작으면 시간을 늘려야하므로 start=mid+1
# 더 적은 시간에도 m명 이상 받을 수 있는지 확인하기 위해 시간을 줄여서 last=mid-1 후 ans 갱신
n,m=map(int,input().split())
p=[int(input()) for _ in range(n)]
start,last,ans=1,10**100,10**100
while start<=last:
    mid=(start+last)//2
    total=0
    for value in p:
        total+=mid//value
    if total<m:
        start=mid+1
    else:
        ans=min(ans,mid)
        last=mid-1
print(ans)
