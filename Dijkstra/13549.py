import sys
from collections import deque
input=sys.stdin.readline
# 25m 15s
# 가장 빠른 시간을 찾아야하기 때문에 0초를 소비하는 2*u를 제일 앞에 둔다.
# i가 1일 때, 2*u와 u+1이 같기 때문에 enumerate를 사용해 index를 이용한다.
n,k=map(int,input().split())
disc=[-1]*100002
disc[n]=0

q=deque()
q.append(n)
while q:
    u=q.popleft()
    for i,v in enumerate([2*u,u-1,u+1]):
        if 0<=v<=100000 and disc[v]==-1:
            if i==0:
                disc[v]=disc[u]
            else:
                disc[v]=disc[u]+1
            q.append(v)
print(disc[k])
