import sys
import heapq
input=sys.stdin.readline
# 59m 38s
# 다익스트라 알고리즘
# bfs에서 deque 대신에 heapq를 써서 최솟값으로만 heap에 넣음
for _ in range(int(input())):
    k,w,h=map(int,input().split())
    dic={}
    for _ in range(k):
        c,t=input().split()
        dic[c]=int(t)

    grid=[]
    sx,sy=0,0
    for i in range(h):
        row=list(map(str,input().rstrip()))
        for j in range(w):
            if row[j]=='E':
                sx,sy=i,j
        grid.append(row)
        
    visited=[[0]*w for _ in range(h)]
    visited[sx][sy]=1
    q=[]
    heapq.heappush(q,[0,sx,sy])
    while q:
        t,x,y=heapq.heappop(q)
        if x==0 or x==h-1 or y==0 or y==w-1:
            print(t)
            break
        for xx,yy in (x,y+1),(x,y-1),(x+1,y),(x-1,y):
            if 0<=xx<h and 0<=yy<w and not visited[xx][yy]:
                visited[xx][yy]=1
                heapq.heappush(q,[t+dic[grid[xx][yy]],xx,yy])
    
