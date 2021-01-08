import sys
input=sys.stdin.readline
def solve(depth,idx):
    if depth==6:
        print(*ans,sep=' ')
        return

    for i in range(idx,k):
        if not visited[i]:
            visited[i]=True
            ans[depth]=S[i]
            solve(depth+1,i)
            visited[i]=False

while True:
    s=list(map(int,input().split()))
    if s[0]==0: break
    k=s[0];S=s[1:]
    visited=[False]*k
    ans=[0]*6
    solve(0,0)
    print()
