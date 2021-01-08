import sys
input=sys.stdin.readline
def solve(depth,idx):
    if depth==M:
        print(*ans,sep=' ')
        return

    for i in range(idx,N+1):
        ans[depth]=i
        solve(depth+1,i)
N,M=map(int,input().split())
ans=[0]*M
solve(0,1)
