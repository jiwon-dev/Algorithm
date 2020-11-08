import sys
from collections import deque
input=sys.stdin.readline
# 11m 54s
L=input().rstrip()
K=input().rstrip()

q=deque()
q.append((L,0))
# (이진수, 동작 횟수)
vis=set()
while q:
    two,cnt=q.popleft()
    if two==K:
        print(cnt)
        break
    for i in range(1,len(two)):
        # 0이면 1로, 1이면 0으로 바꾸어서 vis에 없으면 q와 vis에 넣음
        if two[i]=='0':
            sam=two[:i]+'1'+two[i+1:]
        else:
            sam=two[:i]+'0'+two[i+1:]
        if sam not in vis:
            q.append((sam,cnt+1))
            vis.add(sam)
    ten=int('0b'+two,2)
    # 십진수로 바꿔서 1 더하기, 1 빼기 수행
    for i in [ten-1,ten+1]:
        if 0<=i:
            sam=bin(i)[2:]
            # q에는 이진수의 형태로 넣어야하기 때문에 다시 이진수로 바꾸어서 넣음
            if sam not in vis:
                q.append((sam,cnt+1))
                vis.add(sam)
