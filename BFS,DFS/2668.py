import sys
from collections import deque
input=sys.stdin.readline
# 25m 07s
# dfs로 first는 첫번째 줄에서 선택한 수들의 집합, second는 두번째 줄에서 선택한 수들의 집합
# 처음 틀린 것은 4,3,2,5,1이 반례였음
n=int(input())
graph=[0]*(n+1)
for i in range(1,n+1):
    graph[i]=int(input())

def dfs(s):
    global first
    global second
    first.add(s)
    if not vis[graph[s]]:
        vis[graph[s]]=1
        second.add(graph[s])
        dfs(graph[s])
''' 두개의 집합 안쓰는 버전
    ini=x
    used=set()
    while x not in used:
        used.add(x)
        x=graph[x]
    return x==ini
    '''
ans=[]
for i in range(1,n+1):
    first=set()
    second=set()
    vis=[0]*(n+1)
    dfs(i)
    if first==second: ans.append(i)

if not ans:
    print(0)
else:
    print(len(ans))
    print(*ans,sep='\n')
