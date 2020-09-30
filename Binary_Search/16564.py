import sys
input=sys.stdin.readline
# 10m 36s
# 팀 목표레벨을 가지고 이분 탐색
# 팀 목표레벨이 각 캐릭터의 레벨보다 높으면 (팀 목표레벨-각 캐릭터의 레벨)을 더한다
# 더하는 이유:팀 목표레벨은 레벨을 올렸을 때 팀 내에서 가장 낮은 레벨이므로 현재 캐릭터의 레벨이 팀 목표레벨보다 낮을 경우
# 팀 목표레벨이 가장 낮은 레벨임이 모순된다 따라서 팀 목표레벨까지 올려야 하므로 (팀 목표레벨-각 캐릭터의 레벨)을 해야한다
# 모든 캐릭터가 팀 목표레벨(mid)을 만족하도록 올렸을 경우 total이 K보다 크면 올릴 수 있는 레벨 총합을 넘어서므로 팀 목표레벨을 낮춰야 한다 -> last=mid-1
# K와 작거나 같을 경우는 모든 조건에 만족하므로 더 큰 팀 목표레벨을 설정했을 때도 만족하는지 확인하기 위해 start=mid+1을 해준다
# start를 1로 설정하면 팀에 1이상인 입력만 들어왔을 때 모순이 생길 수 있으므로 모든 캐릭터의 최솟값으로 설정해야한다
# O(log(10^9)*N)
n,k=map(int,input().split())
l=[int(input()) for _ in range(n)]
start,last=min(l),10**9
while start<=last:
    mid=(start+last)//2
    total=0
    for v in l:
        if v<mid:total+=mid-v
    if total<=k:
        start=mid+1
    else:
        last=mid-1
print(last)
