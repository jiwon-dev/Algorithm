import sys
import heapq
input=sys.stdin.readline
# 31m 34s
# 최소 경로는 여러 개가 있을 수 있으므로 아무거나 출력하면 됨
n,m=int(input()),int(input())
D=[[] for _ in range(n+1)]
for _ in range(m):
    u,v,c=map(int,input().split())
    D[u].append((c,v))
s,l=map(int,input().split())

q=[]
path=[-1]*(n+1)
dist=[float('inf')]*(n+1)
dist[s]=0
visited=[False]*(n+1)
heapq.heappush(q,(0,s))

while q:
    w,u=heapq.heappop(q)
    for ww,v in D[u]:
        if dist[v]>w+ww:
            path[v]=u
            dist[v]=w+ww
            heapq.heappush(q,(dist[v],v))

print(dist[l])
ans=[]
while l>=0:
    ans.append(l)
    l=path[l]
print(len(ans))
print(*ans[::-1])
