import sys
from heapq import *
input=sys.stdin.readline
N=int(input())
K=int(input())

H=[[] for _ in range(N)]
for i in range(N):
    M,*t=input().split()
    for j in range(len(t)): t[j]=int(t[j])
    H[i]=t

visited=[[False]*21 for _ in range(N)]
q=[]
heappush(q,(0,-1,1))
# (t 사용 횟수,현재 위치,현재 높이)
while q:
    ans,idx,h=heappop(q)
    if ans>K: continue
    if idx==N-1:
        print(ans)
        sys.exit()
    tmp=len(q)
    for nh in [h,h+1,2*h,h-1]:
        if nh<=0: continue
        if nh>=20: nh=20
        if nh in H[idx+1]:
            if visited[idx+1][nh]: continue
            heappush(q,(ans,idx+1,nh))
            visited[idx+1][nh]=True
    if tmp==len(q):
        for v in H[idx+1]: heappush(q,(ans+1,idx+1,v))
print(-1)
