import sys
input=sys.stdin.readline
# 40m 59s
N,L=map(int,input().split())
T=sorted(list(map(int,input().split())))
# 물이 새는 곳의 위치를 정렬
ans=1
# 처음 새는 곳을 막고 시작하니 ans는 1
tape=T[0]-0.5+L
# tape:커버할 수 있는 최대 공간
for i in range(1,N):
    if T[i]+0.5>tape:
        # 최대로 막아야하는 곳이 커버할 수 있는 최대 공간을 넘어 섰을 경우
        tape=T[i]-0.5+L
        # tape를 늘림(최소로 막아야하는 곳+L)
        ans+=1
        # 테이프를 썼으므로 ans+=1
print(ans)
