import sys
input=sys.stdin.readline
# 13m 37s
# 시간을 기준으로 이분 탐색
# 처음에 틀린 이유:real이 0일 때,division by zero 에러가 떴음 -> real이 0이면 0출력 후 exit
# mid보다 컴퓨터 개수가 많을 경우 mid를 더하고 적을 경우 현재 랙의 컴퓨터 개수를 더함
# (시간이 mid일 때 동작하는 컴퓨터 개수)/(전체 컴퓨터 개수)>=0.5이면 시간을 줄였을 때도 절반이상 켜지는지 확인 위해 last=mid-1
# 아니면 start=mid+1
n=int(input())
c=[list(map(int,input().split())) for _ in range(n)]
real=0
for i in range(n):
    for j in range(n):
        real+=c[i][j]
if real==0:
    print(0)
    sys.exit()
start,last=1,10**10
# 최대 시간은 모든 랙동에 최대 컴퓨터만큼 있을 경우이니 (10**3)*(10**7)=10**10
while start<=last:
    mid=(start+last)//2
    total=0
    for i in range(n):
        for j in range(n):
            if c[i][j]>=mid:
                total+=mid
            else:
                total+=c[i][j]
    if total/real>=0.5:
        last=mid-1
    else:
        start=mid+1
print(start)
