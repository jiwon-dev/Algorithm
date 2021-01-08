import sys
input=sys.stdin.readline
def solve(idx,s):
    if idx==M:
        print(s)
        return

    visited=[False]*(N+1)
    for i in range(N):
        if visited[i]==False:
            visited[i]=True
            solve(idx+1,s+seq[i])
            visited[i]=False
            solve(idx+1,s)
N,M=map(int,input().split())
seq=[str(i) for i in range(1,N+1)]
solve(0,"")
