import sys
input=sys.stdin.readline
# 38m 52s
# 간 레벨을 기준으로 이분 탐색
# 처음에 최대 힙을 만들어서 도수 레벨이 간 레벨보다 작거나 같은 맥주 중 선호도가 제일 높은 순으로 n개를 골랐는데 시간초과
# 어차피 n개를 선택하는 것은 고정이고 도수 레벨이 간 레벨보다 작거나 같은 것 중 선호도가 제일 높은 순으로 n개를 고르면 되니
# 선호도를 내림차순으로 정렬한 뒤, 앞에서부터 살펴보면서 도수 레벨을 만족하는 n개의 맥주를 뽑으면 됨
# 이 때, 도수 레벨을 만족하는 맥주가 n개 미만이거나 도수 레벨을 만족하는게 n개인데 선호도 합이 m미만이면 간 레벨을 올려야하니 start=mid+1
# 도수 레벨을 만족하는 맥주가 n개이고 선호도 합이 m이상이면 모든 조건에 만족하므로 간 레벨을 내려도 만족하는지 구하고 최솟값을 구하기 위해 last=mid-1
# O(log2^31*n)
n,m,k=map(int,input().split())
b=[list(map(int,input().split())) for _ in range(k)]
b.sort(key=lambda x:-x[0])
# 선호도 내림차순으로 정렬
start,last=0,2**31
# 최소는 0, 최대는 2**31
while start<=last:
    sample=n
    # n개를 선택하는지 확인하는 변수
    mid=(start+last)//2
    total=0
    # 선호도 합
    for value in b:
        if sample>0 and value[1]<=mid:
            total+=value[0]
            sample-=1
    if sample>0:
        # 간 레벨을 만족하는 맥주가 n개 미만일 경우(무조건 n개를 마셔야하므로 간 레벨을 늘림)
        start=mid+1
    elif total<m:
        # 간 레벨을 만족하는 맥주가 n개이고 선호도 합이 m미만인 경우(맥주는 다 마셨으나 선호도가 다 채워지지 않았으므로 간 레벨을 늘림)
        start=mid+1
    else:
        # 위 조건을 다 만족하면 간 레벨을 낮춰도 조건들을 만족하는지 확인(최솟값 확인하기 위해 범위를 줄임)
        last=mid-1
print(-1 if start>=2**31 else start)
