import sys
from collections import deque
input=sys.stdin.readline
# 23m
for _ in range(int(input())):
    N=int(input())
    C=input().split()
    q=deque()
    q.append(C[0])

    for i in range(1,N):
        if q[0]>=C[i]: q.appendleft(C[i])
        else: q.append(C[i])
    print("".join(q))
