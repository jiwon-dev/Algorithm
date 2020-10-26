import sys
import heapq
input=sys.stdin.readline
# 15m 12s
# 다익스트라
# heap에 [부순 횟수,x좌표,y좌표]
n=int(input())
grid=[list(map(int,input().rstrip())) for _ in range(n)]
visited=[[0]*n for _ in range(n)]
q=[]
heapq.heappush(q,[0,0,0])
while q:
    chg,x,y=heapq.heappop(q)
    if x==n-1 and y==n-1:
        print(chg)
        break
    for xx,yy in (x,y+1),(x,y-1),(x+1,y),(x-1,y):
        c=chg
        if 0<=xx<n and 0<=yy<n and not visited[xx][yy]:
            visited[xx][yy]=1
            if not grid[xx][yy]:
                c+=1
            heapq.heappush(q,[c,xx,yy])
    

