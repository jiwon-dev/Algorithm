import sys
from collections import deque
input=sys.stdin.readline
N=int(input())
book=deque([int(input()) for _ in range(N)])
res=deque([i for i in range(1,N+1)])
if book==res:
    print(0)
    sys.exit()
ans=0
while N>=1:
    if book[0]!=N:
        ans+=1
        book.appendleft(N)
    N-=1
print(ans)
