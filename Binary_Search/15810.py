import sys
input=sys.stdin.readline
# 13m 56s
# 시간을 가지고 이분 탐색
# 각 풍선별 전체 시간//풍선 부는데 걸리는 시간을 다 더해서 m보다 작으면 시간을 늘리고 크거나 같으면 시간을 줄임
n,m=map(int,input().split())
b=list(map(int,input().split()))
start,last=1,10**12
while start<=last:
    mid=(start+last)//2
    total=0
    for value in b:
        total+=mid//value
    if total<m:
        start=mid+1
    else:
        last=mid-1
print(start)
