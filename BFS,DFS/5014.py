import sys
from collections import deque
input=sys.stdin.readline
# 05m 13s
# disc 1차원 배열을 두어 눌러야하는 버튼의 최솟값을 넣음
# 선택지는 올라가는 것과 내려가는 것 두개 밖에 없음
F,S,G,U,D=map(int,input().split())
disc=[-1]*(F+1)

q=deque()
q.append(S)
disc[S]=0
while q:
    n=q.popleft()
    for v in (n+U),(n-D):
        if 1<=v<=F and disc[v]==-1:
            disc[v]=disc[n]+1
            q.append(v)
print('use the stairs' if disc[G]==-1 else disc[G])
