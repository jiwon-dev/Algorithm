import sys
from collections import deque
input=sys.stdin.readline
sys.setrecursionlimit(100000000)
# 20m 18s
# bfs 이용
dx,dy=[-1,-2,1,2,-2,-1,2,1],[-2,-1,-2,-1,1,2,1,2]
# 나이트 이동 반경에 따라 dx,dy 정함
def bfs(x,y):
    q=deque([[x,y]])
    visited[x][y]=1
    count=0
    if x==t1 and y==t2:
        return count
    while q:
        count+=1
        # 밑에 for문을 다 돌면 노드의 모든 인접노드들을 다 살펴 본 경우이므로 count+=1
        for i in range(len(q)):
            a,b=q.popleft()
            for j in range(8):
                aa,bb=a+dx[j],b+dy[j]
                if aa==t1 and bb==t2:
                    return count
                if 0<=aa<l and 0<=bb<l and not visited[aa][bb]:
                    q.append([aa,bb])
                    visited[aa][bb]=1
                    
for _ in range(int(input())):
    l=int(input())
    visited=[[0]*l for _ in range(l)]
    x,y=map(int,input().split())
    t1,t2=map(int,input().split())
    print(bfs(x,y))
