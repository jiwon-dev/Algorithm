import sys
from collections import deque
input=sys.stdin.readline
# 1시간 이상
# 루트 노드는 1로 고정되있으니 1부터 시작해서 dfs 실행하면서 parents(부모 노드 저장하는 리스트)에 부모 노드 저장
sys.setrecursionlimit(10**9)
n=int(input())
graph=[[] for _ in range(n+1)]
parents=[0]*(n+1)
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
def dfs(s):
    for i in graph[s]:
        if parents[i]==0:
            parents[i]=s
            dfs(i)
dfs(1)
for i in range(2,n+1):
    print(parents[i])
    
