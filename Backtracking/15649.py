import sys
input=sys.stdin.readline
def solve(idx,s):
    if idx==M:
        for v in s: print(v,end=' ')
        print()
        return

    for i in range(N):
        if not visited[i]:
            visited[i]=True
            solve(idx+1,s+seq[i])
            visited[i]=False
N,M=map(int,input().split())
seq=[str(i) for i in range(1,N+1)]
visited=[False]*(N+1)
solve(0,"")
