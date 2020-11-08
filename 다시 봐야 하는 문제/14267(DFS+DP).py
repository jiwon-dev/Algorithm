import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
cel=list(map(int,input().split()))
for i in range(1,n):
    graph[cel[i]].append(i+1)

ans=[0]*(n+1)
for _ in range(m):
    a,b=map(int,input().split())
    ans[a]+=b
    
def dfs(s,p):
    ans[s]+=ans[p]
    for v in graph[s]:
        dfs(v,s)
dfs(1,1)
print(*ans[1:],sep=' ')
