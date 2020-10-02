import sys
from collections import deque
# dx,dy를 이용해 상하좌우 좌표를 만들어놓고 'W'일때 상하좌우 살펴봐서 'S'가 있으면 양을 못지키니 True
# 주의할 점:15행을 try,except를 쓰면 안됨 -> 파이썬은 -1행과 -1열이 존재하기 때문에 틀린 값을 출력함
# 최소 개수의 사다리를 사용하는게 아니기 때문에 모든 빈칸을 사다리로 덮어도 됨
input=sys.stdin.readline
r,c=map(int,input().split())
m=[input().rstrip() for _ in range(r)]
dx,dy=[-1,1,0,0],[0,0,-1,1]
ck=False
for i in range(r):
    for j in range(c):
        if m[i][j]=='W':
            for k in range(4):
                ii,jj=i+dx[k],j+dy[k]
                if ii<0 or ii==r or jj<0 or jj==c:
                    continue
                if m[ii][jj]=='S':
                    ck=True
if ck:
    print(0)
else:
    print(1)
    for i in range(r):
        for j in range(c):
            if m[i][j]=='.':
                print('D',end='')
            else:
                print(m[i][j],end='')
        print()
