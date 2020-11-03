import sys
import heapq
input=sys.stdin.readline
dx,dy=[-1,1,0,0],[0,0,-1,1]
# 위,아래,왼,우
# 입구, 출구의 다익스트라에 따라 결과가 달라질 수 있으므로 두번 실행
n=int(input())
grid=[list(map(str,input().rstrip())) for _ in range(n)]
door=[(x,y) for x in range(n) for y in range(n) if grid[x][y]=='#']
sx,sy,ex,ey=door[0][0],door[0][1],door[1][0],door[1][1]

def dijk(sx,sy,ex,ey):
    q=[]
    for i in range(4):
        xx,yy=sx+dx[i],sy+dy[i]
        if 0<=xx<n and 0<=yy<n:
            if grid[xx][yy]=='.': heapq.heappush(q,(0,xx,yy,i))
            elif grid[xx][yy]=='!': heapq.heappush(q,(1,xx,yy,i))
            
    while q:
        cnt,x,y,d=heapq.heappop(q)
        while 1:
            if not (0<=x<n and 0<=y<n): break
            if x==ex and y==ey: return cnt
            if grid[x][y]=='*': break
            elif grid[x][y]=='!':
                if d in [0,1]:
                    for k in range(2,4):
                        xx,yy=x+dx[k],y+dy[k]
                        heapq.heappush(q,(cnt+1,xx,yy,k))
                else:
                    for k in range(0,2):
                        xx,yy=x+dx[k],y+dy[k]
                        heapq.heappush(q,(cnt+1,xx,yy,k))
                break
            else:
                x,y=x+dx[d],y+dy[d]               
print(min(dijk(sx,sy,ex,ey),dijk(ex,ey,sx,sy)))
