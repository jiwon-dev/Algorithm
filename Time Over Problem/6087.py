import sys
import heapq
input=sys.stdin.readline
# 1시간 이상
w,h=map(int,input().split())
grid=[list(map(str,input().rstrip())) for _ in range(h)]
mirror=[(y,x) for y in range(h) for x in range(w) if grid[y][x]=='C']
sx,sy=mirror[0]
ex,ey=mirror[1]
dx,dy=[-1,0,1,0],[0,-1,0,1]

def dijkstra(sx,sy,ex,ey):
    q=[]
    heapq.heappush(q,[-1,-1,sx,sy])
    visited=[[float('inf')]*w for _ in range(h)]
    visited[sx][sy]=0
    while q:
        cnt,p,x,y=heapq.heappop(q)
        if x==ex and y==ey:
            return cnt
        for i in range(4):
            c=cnt
            xx,yy=x+dx[i],y+dy[i]
            if 0<=xx<h and 0<=yy<w and visited[xx][yy]>cnt and grid[xx][yy] in '.C':
                if p!=i:
                    c+=1
                visited[xx][yy]=c
                heapq.heappush(q,[c,i,xx,yy])
print(min(dijkstra(sx,sy,ex,ey),dijkstra(ex,ey,sx,sy)))
