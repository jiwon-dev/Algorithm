import sys
from collections import deque
input=sys.stdin.readline
# 11m 33s
# 최솟값이므로 bfs 이용
a,b=map(int,input().split())

q=deque([a])
ans=0
while q:
    ans+=1
    for _ in range(len(q)):
        u=q.popleft()
        sam=[2*u,10*u+1]
        # [2를 곱한 수랑, 수의 가장 오른쪽에 1을 추가한 수] 리스트를 만든다
        for i in range(2):
            if sam[i]==b:
                # 둘 중에 b를 만들 수 있으면 횟수 출력하고 종료
                print(ans+1)
                sys.exit()
            elif 1<=sam[i]<=10**9:
                # b를 만들 수 없는데 1과 10**9 사이면 만들 때 까지 살펴봐야하므로 q에 추가
                q.append(sam[i])
            else:
                # 10**9를 넘으면 두 가지 선택지 모두 수가 커지는 경우이므로 b를 만들 수 없으므로 continue
                # continue를 하는 이유:둘 중에 답이 나올 수 있는데 -1을 출력하고 종료해버리면 답이 나오는데도 -1로 출력하는 경우가 있음
                continue
print(-1)
