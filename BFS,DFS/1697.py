import sys
from collections import deque
input=sys.stdin.readline
# bfs와 count 안쓰고 리스트로 해결
# i의 범위 조심하기
n,k=map(int,input().split())
disc=[-1]*100001
disc[n]=0
q=deque([n])
while q:
    s=q.popleft()
    for i in [s-1,s+1,2*s]:
        if 0<=i<=100000 and disc[i]==-1:
            disc[i]=disc[s]+1
            q.append(i)
print(disc[k])
