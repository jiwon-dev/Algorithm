import sys
import heapq
input=sys.stdin.readline
# 19m 42s
# 갈 수 있는 모든 경로와 비용을 구한 다음 다익스트라
# 갈 수 있는 경로:1->2~N,2->3~N,3->4~N...
N=int(input())
F=[input().rstrip() for _ in range(N)]
D=[[] for _ in range(N)]

for i in range(N):
    for j in range(i+1,N):
        dif=0
        for k in range(len(F[i])):
            dif+=abs(int(F[i][k])-int(F[j][k]))**2
        D[i].append((dif,j))
        D[j].append((dif,i))
        # 양방향

s,l=map(int,input().split())
s-=1;l-=1
q=[]
dist=[float('inf')]*N
dist[s]=0
visited=[False]*N
heapq.heappush(q,(0,s))

while q:
    w,u=heapq.heappop(q)
    if visited[u]==True: continue
    for ww,v in D[u]:
        if dist[v]>w+ww:
            dist[v]=w+ww
            heapq.heappush(q,(dist[v],v))
    visited[u]=True

print(dist[l])


