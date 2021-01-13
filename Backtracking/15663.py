import sys
input=sys.stdin.readline
def solve(depth,s):
    global ans
    global union
    if depth==M:
        if s not in union:
            print(*ans)
            union.add(s)
        return

    for i in range(N):
        if not visited[i]:
            visited[i]=True
            ans[depth]=seq[i]
            solve(depth+1,s+str(seq[i]))
            visited[i]=False

N,M=map(int,input().split())
seq=list(map(int,input().split()))
seq.sort()
union=set()
ans=[0]*M
visited=[False]*len(seq)
solve(0,"")

