import sys
from collections import deque
input=sys.stdin.readline
# 56m 49s
# disc는 출발지부터 위치까지 쓴 힘의 크기
for _ in range(int(input())):
    h,w,o,f,sx,sy,ex,ey=map(int,input().split())
    grid=[[0]*w for _ in range(h)]
    disc=[[-1]*w for _ in range(h)]
    for _ in range(o):
        x,y,l=map(int,input().split())
        grid[x-1][y-1]=l
    sx-=1; sy-=1; ex-=1; ey-=1
    q=deque()
    q.append([sx,sy])
    disc[sx][sy]=0
    while q:
        a,b=q.popleft()
        for aa,bb in (a,b+1),(a,b-1),(a-1,b),(a+1,b):
            if not (0<=aa<h and 0<=bb<w): continue
            if disc[aa][bb]!=-1: continue
            if grid[aa][bb]-grid[a][b]>f-disc[a][b]: continue
            disc[aa][bb]=disc[a][b]+1
            q.append([aa,bb])
    print('잘했어!!' if disc[ex][ey]!=-1 else '인성 문제있어??')
