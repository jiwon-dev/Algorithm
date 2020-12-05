import sys
import heapq
input=sys.stdin.readline
# 13m 35s
# O(N^2logM)
def dijkstra(arr,start):
    q=[]
    dist=[float('inf')]*(N+1)
    dist[start]=0
    heapq.heappush(q,(0,start))

    while q:
        w,u=heapq.heappop(q)
        for ww,v in D[u]:
            if dist[v]>dist[u]+ww:
                dist[v]=dist[u]+ww
                heapq.heappush(q,(dist[v],v))

    for i in range(1,N+1):
        arr[i]+=dist[i]
    return arr

for _ in range(int(input())):
    N,M=map(int,input().split())
    D=[[] for _ in range(N+1)]
    for _ in range(M):
        a,b,c=map(int,input().split())
        D[a].append((c,b))
        D[b].append((c,a))
        # 양방향

    K=int(input())
    F=list(map(int,input().split()))
    
    ans=[float('inf')]+[0]*N
    for v in F:
        # 각 친구별 이동 거리의 합을 ans에 담음(idx가 방 번호)
        ans=dijkstra(ans,v)
    print(ans.index(min(ans)))
