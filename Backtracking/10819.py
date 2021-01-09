import sys
input=sys.stdin.readline
def solve(depth):
    global ans
    if depth==N:
        temp=0
        for i in range(N-1): temp+=abs(seq[idx[i]]-seq[idx[i+1]])
        ans=max(ans,temp)
        return

    for i in range(N):
        if not visited[i]:
            visited[i]=True
            idx[depth]=i
            solve(depth+1)
            visited[i]=False

N=int(input())
seq=list(map(int,input().split()))
ans=-float('inf')
visited=[False]*N
idx=[0]*N
solve(0)
print(ans)
