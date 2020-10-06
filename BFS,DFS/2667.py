import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
# 09m 44s
# 총 단지 수:처음 dfs 호출 횟수(재귀 제외)
# 각 단지내 집 수:dfs 재귀 호출 횟수
n=int(input())
MAP=[list(map(int,input().rstrip())) for _ in range(n)]
visited=[[0]*n for _ in range(n)]
result,count=[],0
dx,dy=[-1,1,0,0],[0,0,-1,1]

def dfs(x,y):
    global cnt
    cnt+=1
    visited[x][y]=1
    for i in range(4):
        xx,yy=x+dx[i],y+dy[i]
        if 0<=xx<n and 0<=yy<n and MAP[xx][yy] and not visited[xx][yy]:
            visited[xx][yy]=1
            dfs(xx,yy)

for i in range(n):
    for j in range(n):
        if MAP[i][j] and not visited[i][j]:
            cnt=0
            dfs(i,j)
            count+=1
            result.append(cnt)
result.sort()
print(count)
print(*result,sep='\n')
            
    
