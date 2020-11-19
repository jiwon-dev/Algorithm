import sys
from collections import deque
input=sys.stdin.readline
# 20m 37s
# 덱을 이용한 그리디
for _ in range(int(input())):
    N=int(input())
    H=sorted(map(int,input().split()))
    # 왼쪽에서 넣기->오른쪽에서 넣기를 반복할 것이기 때문에 정렬
    q=deque()
    # 왼쪽과 오른쪽에서 넣을 것이므로 덱을 사용
    for i in range(N):
        # 짝수이면 왼쪽에서, 홀수이면 오른쪽에서 넣음
        if i%2==0: q.appendleft(H[i])
        else: q.append(H[i])
    # 위의 과정을 통해 각 인접한 통나무의 높이 차가 최소가 되게 만듬
    ans=0
    for j in range(N-1):
        # 서로 인접한 통나무의 높이 차 중 최댓값을 구해야하므로 ans 갱신
        ans=max(ans,abs(q[j]-q[j+1]))
    print(ans)
