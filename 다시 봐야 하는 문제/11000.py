# 회의실 배정과 비슷한 문제이지만 이 문제는 모든 수업을 해야하기 때문에 시작 시간을 우선으로 정렬한다.
# -> 시작 시간이 빠른 순서대로 정렬해야 최소 강의실로 모든 수업을 할 수 있기 때문
from heapq import *
pq=[]
N=int(input())
l=[list(map(int,input().split())) for _ in range(N)]
l.sort(key=lambda x:[x[0],x[1]])
for a,b in l:
    if not pq: heappush(pq,b)
    elif pq[0]<=a: heappop(pq); heappush(pq,b)
    else: heappush(pq,b)
print(len(pq))



        
            
