import sys
from heapq import *
input=sys.stdin.readline
# 46m
# 0을 고려하지 않아서 틀렸음
# 양수는 최대힙, 음수는 최소힙을 돌려야함
N=int(input())
pos,neg=[],[]
# 양수 최대힙, 음수 최소힙
def chg(i,t):
    # (수열의 수, t==0이면 음수이고 t==1이면 양수를 나타내는 타입값)
    if t==1: return -i
    # 양수일 때는 최대힙이고 -i로 삽입했기 때문에 원래 값인 -i 리턴
    # 음수일 때는 최소힙이므로 그대로 i 리턴
    return i

def solve(q,t):
    # (t==0이면 neg, t==1이면 pos)
    global ans
    while True:
        if not q: break
        # 힙이 비었으면 break
        if len(q)==1:
            # 힙에 하나의 수만 남아있다면 원래 값으로 변환한 뒤, ans에 추가
            ans.append(chg(heappop(q),t))
            break
        a,b=chg(heappop(q),t),chg(heappop(q),t)
        # 두 개의 수를 묶어야되는지 확인하기 위해 두 개의 수를 꺼내고 원래 값으로 나타냄
        if a+b<a*b: ans.append(a*b)
        # 묶지 않았을 때(더하기)<묶었을 때(곱하기)이면 묶은 값을 ans에 추가
        else: ans.append(a+b)
        # 아니면 묶지 않은 값(더하기)를 ans에 추가

for _ in range(N):
    l=int(input())
    if l<=0: heappush(neg,l)
    # 핵심
    # 최대의 합을 구해야하기 때문에 0을 neg에 넣어야함. <- 부등호를 넣지 않아서 계속 틀렸음
    else: heappush(pos,-l)
    # 양수는 pos에 넣음

ans=[]
solve(pos,1); solve(neg,0)
# 양수, 음수에 대해 따로 solve 실행
print(sum(ans))
# ans의 합이 정답임
