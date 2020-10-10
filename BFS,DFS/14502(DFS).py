import sys
from collections import deque
sys.setrecursionlimit(10**9)
input=sys.stdin.readline
# DFS의 장점:큐를 사용하지 않기 때문에 따로 초기 큐를 받을 필요가 없다
n,m=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(n)]
memory=[]
zero=[(y,x) for y in range(n) for x in range(m) if not grid[y][x]]
virus=[(y,x) for y in range(n) for x in range(m) if grid[y][x]==2]
# 리스트에도 조건문 사용 가능
for i in range(n):
    sam=[]
    for j in range(m):
        sam.append(grid[i][j])
    memory.append(sam)

def initiate():
    for i in range(n):
        for j in range(m):
            grid[i][j]=memory[i][j]

def cal():
    cnt=0
    for i in range(n):
        for j in range(m):
            if not grid[i][j]:
                cnt+=1
    return cnt

def dfs(y,x):
    # dfs로 4방향 재귀호출함
    # 주의:인덱스 에러 뜨면 리턴, 계산이 필요없는것도 리턴
    if not 0<=y<n or not 0<=x<m:return
    if grid[y][x]:return
    grid[y][x]=2
    
    dfs(y-1,x)
    dfs(y+1,x)
    dfs(y,x-1)
    dfs(y,x+1)

ans=0       
for i in range(len(zero)):
    for j in range(i+1,len(zero)):
        for k in range(j+1,len(zero)):
            grid[zero[i][0]][zero[i][1]]=1
            grid[zero[j][0]][zero[j][1]]=1
            grid[zero[k][0]][zero[k][1]]=1
            for y,x in virus:
                grid[y][x]=0
                dfs(y,x)
            ans=max(ans,cal())
            initiate()
print(ans)
