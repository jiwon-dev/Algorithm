import sys
input=sys.stdin.readline
def solve(depth):
    if depth==M:
        print(*ans,sep=' ')
        return

    for i in range(1,N+1):
        ans[depth]=i
        solve(depth+1)
N,M=map(int,input().split())
ans=[0]*M
solve(0)
