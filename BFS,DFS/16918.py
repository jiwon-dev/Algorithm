import sys
from collections import deque
input=sys.stdin.readline
# 35m 30s
# bfs인데 visited 쓰지 않음
r,c,n=map(int,input().split())
MAP=[list(map(str,input().rstrip())) for _ in range(r)]
dx,dy=[-1,1,0,0],[0,0,-1,1]
# 폭탄이 설치된 시간이 MAP[i][j]에 들어감
# 초기 폭탄은 0의 값을 가짐
for i in range(r):
    for j in range(c):
        if MAP[i][j]=='O':
            MAP[i][j]=0
            
def bomb(cnt):
    # (폭탄 설치 시간)
    # MAP에서 빈 곳에 폭탄을 설치하는 함수
    # MAP에는 빈칸 아니면 폭탄이 설치된 시간의 값을 가짐
    for i in range(r):
        for j in range(c):
            if MAP[i][j]=='.':
                MAP[i][j]=cnt

def bfs(x,y,l):
    # (x좌표,y좌표,폭탄 터지는 시간)
    # bfs 함수는 폭탄이 터질 때 상하좌우에서 동시에 터지는 폭탄이 아니면(폭탄 터지는 시간이 x,y랑 다르면)
    # 빈칸으로 만들고 폭탄 터지는 시간이 같으면 그대로 놔둠
    MAP[x][y]='.'
    for i in range(4):
        xx,yy=x+dx[i],y+dy[i]
        if 0<=xx<r and 0<=yy<c and MAP[xx][yy]!=l:
            MAP[xx][yy]='.'

start=2
# 초기 시작은 1초부터 시작이니 2초에 활동 시작
for i in range(start,n+1):
    # i:시간
    if i%2!=0:
        # 홀수 시간이면 폭탄이 터져야 하니 bfs 함수 실행
        for j in range(r):
            for k in range(c):
                if MAP[j][k]==i-3:
                    # MAP[j][k]가 터져야 하는 폭탄이면 
                    bfs(j,k,i-3)
                    # bfs를 실행해 상하좌우 터트림
    else:
        # 짝수 시간이면 새로운 폭탄을 설치해야하므로 bomb 함수 실행
        bomb(i)
        
for i in range(r):
    for j in range(c):
        if MAP[i][j]!='.':
            print('O',end='')
        else:
            print('.',end='')
    print()



