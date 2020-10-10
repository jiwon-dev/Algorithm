import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline
# 13m 12s
# dfs 이용
# 일반인과 적록색맹에 해당하는 그리드를 2개 만들어 dfs를 2번 돌림
n=int(input())
grid=[list(map(str,input().rstrip())) for _ in range(n)]
n_grid=[]
dx,dy=[-1,1,0,0],[0,0,-1,1]

for i in range(n):
    sam=[]
    for j in range(n):
        if grid[i][j]=='G':sam.append('R')
        else:sam.append(grid[i][j])
    n_grid.append(sam)

def dfs(x,y,c,g,v):
    for i in range(4):
        xx,yy=x+dx[i],y+dy[i]
        if 0<=xx<n and 0<=yy<n and not v[xx][yy] and g[xx][yy]==c:
            v[xx][yy]=1
            dfs(xx,yy,c,g,v)

def cal(g):
    cnt=0
    v=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not v[i][j]:
                dfs(i,j,g[i][j],g,v)
                cnt+=1
    return cnt
                
one=cal(grid)
two=cal(n_grid)
print(one,two)
