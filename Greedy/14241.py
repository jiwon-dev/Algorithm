import sys
import heapq
# 05m 33s
# 최대 힙 사용
input=sys.stdin.readline
N=int(input())
S=list(map(int,input().split()))
q=[]
for v in S:
    heapq.heappush(q,-v)
ans=0
while len(q)>1:
    x=heapq.heappop(q)
    y=heapq.heappop(q)
    ans+=abs(x*y)
    heapq.heappush(q,x+y)
print(ans)
