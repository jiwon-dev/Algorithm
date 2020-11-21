import sys
input=sys.stdin.readline
# 10m 29s
# 거꾸로 뒤집어서 파는 날(최대 가격)을 정하고 최대 가격보다 작은 가격이 나올 경우 차익(최대 가격-현재 가격)을 P에 기록
# 최대 가격보다 큰 가격이 나올 경우 최대 이익을 내야하므로 파는 날(최대 가격)을 갱신
# P를 안쓰고 변수 하나로만 풀수도 있음
for _ in range(int(input())):
    N=int(input())
    D=list(map(int,input().split()))[::-1]
    P=[0]*N
    max_value=D[0]
    for i,v in enumerate(D[1:]):
        if v>=max_value:
            max_value=v
        else:
            P[i]=max_value-v
    print(sum(P))
