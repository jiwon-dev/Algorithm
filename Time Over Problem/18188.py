import sys
from collections import deque
input=sys.stdin.readline
# 1시간 이상
# bfs(x좌표,y좌표,지나온 흔적(str))
h,w=map(int,input().split())
grid=[list(map(str,input().rstrip())) for _ in range(h)]
disc=[[0]*w for _ in range(h)]
s_x,s_y,l_x,l_y=0,0,0,0
trans={}
trans['W']=[-1,0];trans['S']=[1,0];trans['A']=[0,-1];trans['D']=[0,1]
direction={}
direction[(-1,0)]='W';direction[(1,0)]='S';direction[(0,-1)]='A';direction[(0,1)]='D'
for i in range(h):
    for j in range(w):
        if grid[i][j]=='D':
            s_x,s_y=i,j
        if grid[i][j]=='Z':
            l_x,l_y=i,j

order={}
n=int(input())
for i in range(n):
    l=input().split()
    order[i+1]=[]
    for c in l:
        order[i+1].append(trans[c])

ans=[]
q=deque()
q.append([s_x,s_y,""])
time=0
while q:
    time+=1
    for _ in range(len(q)):
        a,b,ans=q.popleft()
        if a==l_x and b==l_y:
            print('YES')
            print(ans)
            sys.exit()
        if time>n:continue
        for x,y in order[time]:
            sam=ans[:]
            aa,bb=a+x,b+y
            if 0<=aa<h and 0<=bb<w and grid[aa][bb]!='@':
                sam+=direction[(x,y)]
                q.append([aa,bb,sam])
print('NO')
    

