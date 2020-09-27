import sys
input=sys.stdin.readline
# 22m 06s
# result에는 각 d값당 [d[i]-mid,d[i]+mid]가 들어가 있음
# result를 쓰는 이유:현재 등의 최소 범위가 이전 등의 최대 범위보다 작거나 같아야
# 이전 등의 최소 범위부터 현재 등의 최대 범위까지 빈틈없이 비출 수 있음
# 만약 현재 등의 최소 범위가 이전 등의 최대 범위보다 크면 빈틈이 생기기 때문에 check=1후 break
# 또, 등을 끝까지 살펴보았을 때, 제일 첫번째등의 최소범위가 0이하이고 제일 마지막 등의 최대 범위가 n이상이어야 빈틈이 없이
# 0~n까지 비출 수 있으므로 22행에서 한번 더 체크해줌
n=int(input())
m=int(input())
d=list(map(int,input().split()))
start,last=1,10**6
# 최소, 최대는 각각 1,10**6
while start<=last:
    mid=(start+last)//2
    check=0
    # 등을 확인하다가 중간에 빈틈이 생기면 체크하는 변수
    result=[[0,10**6]]
    # 제일 처음 값을 쉽게 비교하기 위해 값을 하나 넣어두고 시작
    for i in range(m):
        if d[i]-mid>result[i][1]:
            # 7행에 있는 내용처럼 이전 등의 최대 범위가 현재 등의 최소 범위보다 작을 때 빈틈이 생기므로
            # 뒤에 있는 등은 확인 할 필요가 없다. 따라서 check=1후 탈출
            check=1
            break
        result.append([d[i]-mid,d[i]+mid])
        # 이때까지 확인한 등들의 빈틈이 없으므로 result에 [현재 등 최소범위,현재 등 최대범위] 추가
    if check==0 and result[1][0]<=0 and result[-1][1]>=n:
        # 빈틈이 생기지 않고 첫번째 등의 최소범위가 0이하, 마지막 등의 최대범위가 n이상이면 0~n까지 밝으므로
        # 최소 높이를 구하는 문제이고 높이를 낮춰도 0~n까지 비출 수 있는지 확인하기 위해 last=mid-1
        last=mid-1
    else:
        # 빈틈이 생겼으면 높이를 더 높여야 하므로 start=mid+1
        start=mid+1
print(start)
