import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
# 10m 20s
# 바깥쪽은 행의 인덱스가 0일 때이고 바깥쪽에서 전류를 흘려주니 MAP[0][j]가 0일 때 dfs 실행
# 상하좌우 -> dx,dy, 전류가 통하는 값은 0이므로 not MAP[xx][yy]
m,n=map(int,input().split())
MAP=[list(map(int,input().rstrip())) for _ in range(m)]
visit=[[0]*n for _ in range(m)]
dx,dy=[-1,1,0,0],[0,0,-1,1]

def dfs(x,y):
    stk=[[x,y]]
    while stk:
        a,b=stk.pop()
        for i in range(4):
            aa,bb=a+dx[i],b+dy[i]
            if 0<=aa<m and 0<=bb<n and not MAP[aa][bb] and not visit[aa][bb]:
                stk.append([aa,bb])
                visit[aa][bb]=1
            
for j in range(n):
    if not MAP[0][j]:
        dfs(0,j)
        
if visit[-1].count(1)>0:print('YES')
else:print('NO')
