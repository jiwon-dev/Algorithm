import sys
input=sys.stdin.readline
# 48m (2)
dic={'S':(1,0),'E':(0,1),'W':(0,-1),'N':(-1,0)}
L=int(input())
O=input().rstrip()

visited=[[False]*2000 for _ in range(2000)]
visited[550][550]=True
x,y=550,550

idx=0
while idx<L:
    x,y=x+dic[O[idx]][0],y+dic[O[idx]][1]
    visited[x][y]=True
    idx+=1

ans=0
for i in range(2000):
    for j in range(2000):
        if visited[i][j]:
            ans+=1
print(ans)
