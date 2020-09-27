import sys
input=sys.stdin.readline
# 힌트를 얻고 문제 품
# 최대 거리를 가지고 이분탐색함
# parametric search
n,c=map(int,input().split())
h=sorted(int(input()) for _ in range(n))
start,last=1,h[-1]
# start는 답이 될 수 있는 최소 거리, last는 답이 될 수 있는 최대 거리
while start<=last:
    mid=(start+last)//2
    cnt=1
    # cnt는 공유기 설치 개수
    # 첫번째 집은 무조건 설치 해야하므로 cnt=1로 초기화
    first=h[0]
    for value in h:
        # mid 거리 유지하면서 설치할 수 있는 최대 공유기 개수 파악
        if value-first>=mid:
            first=value
            cnt+=1
    if cnt<c:
        # 답이 mid일 때 공유기 설치 개수가 c보다 작을 경우
        # 거리를 줄여야하므로 last=mid-1
        last=mid-1
    else:
        # c보다 같거나 클 경우
        start=mid+1
        # 최대 거리를 구해야하므로 start=mid+1
print(last)
