import sys
input=sys.stdin.readline
# 07m 54s
def prime_list(n):
    # 에라토스테네스의 체
    check=[True]*n
    m=int(n**0.5)
    for i in range(2,m+1):
        if check[i]==True:
            for j in range(i+i,n,i):
                check[j]=False
    return [i for i in range(2,n) if check[i]==True]

def solve(depth,idx,res):
    global ans
    if depth==M:
        # M개의 수를 선택했다면
        if res in prime: ans.add(res)
        # 소수이면 ans에 넣고 return
        return
    
    for i in range(idx,N):
        if not visited[i]:
            # 방문하지 않았다면
            visited[i]=True
            # 방문 표시 후
            solve(depth+1,i,res+cow[i])
            # 방문
            visited[i]=False
            # 다 방문했으니 백트래킹

N,M=map(int,input().split())
cow=list(map(int,input().split()))
ans=set()
prime=prime_list(9000)
visited=[False]*N
solve(0,0,0)
ans=sorted(ans)
if not ans: print(-1)
else: print(*ans)
