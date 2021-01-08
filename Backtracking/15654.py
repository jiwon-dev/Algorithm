import sys
input=sys.stdin.readline
def solve(depth):
    if depth==M:
        print(*ans,sep=' ')
        return

    for i in range(N):
        if not visited[i]:
            visited[i]=True
            ans[depth]=seq[i]
            solve(depth+1)
            visited[i]=False

N,M=map(int,input().split())
seq=list(map(int,input().split()))
seq.sort()
ans=[0]*M
visited=[False]*(N+1)
solve(0)
