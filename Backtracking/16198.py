import sys
input=sys.stdin.readline
# 19m 15s
def solve(depth,res):
    global ans
    if depth==N-2:
        ans=max(ans,res)
        return

    for i in range(1,N-1):
        if not visited[i]:
            visited[i]=True
            left,right=0,0
            # 방문했으면 지워진 값이므로 방문하지 않은 인덱스 중 i와 가장 붙어있는 왼쪽, 오른쪽 인덱스
            for j in range(i,-1,-1):
                if not visited[j]:
                    left=j
                    break
            for k in range(i,N):
                if not visited[k]:
                    right=k
                    break
            solve(depth+1,res+seq[left]*seq[right])
            visited[i]=False
N=int(input())
seq=list(map(int,input().split()))
ans=0
visited=[False]*N
solve(0,0)
print(ans)
