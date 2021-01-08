import sys
input=sys.stdin.readline
def solve(depth,idx):
    if depth==M:
        print(*ans,sep=' ')
        return

    for i in range(idx,N):
        if not visited[i]:
            visited[i]=True
            ans[depth]=seq[i]
            solve(depth+1,i)
            visited[i]=False
        
N,M=map(int,input().split())
seq=[i for i in range(1,N+1)]
visited=[False]*(N+1)
ans=[0]*M
solve(0,0)
