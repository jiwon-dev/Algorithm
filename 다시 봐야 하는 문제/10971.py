import sys
input=sys.stdin.readline
# 1시간 이상
def solve(depth,first,prev,cost):
    global ans
    if depth==N:
        # 모든 도시를 다 방문했을 때
        if W[prev][first]!=0: ans=min(ans,cost+W[prev][first])
        # 마지막 도시에서 시작 도시로의 경로가 존재할 때만 ans 갱신해줘야함
        # 계속 틀린 이유도 마지막 도시에서 시작 도시의 경로가 없는데 갱신해줘서 틀렸음
        return

    for i in range(N):
        if not visited[i] and W[prev][i]!=0:
            # 방문한 적없고 prev->i의 경로가 있을 때
            visited[i]=True
            # 방문 체크
            solve(depth+1,first,i,cost+W[prev][i])
            # 다른 도시로 방문을 위한 재귀
            visited[i]=False
            # 하나의 여행 경로가 완성됐으니 백트래킹으로 되돌려줌

N=int(input())
W=[list(map(int,input().split())) for _ in range(N)]
ans=float('inf')
visited=[False]*N
for i in range(N):
    # 시작 도시를 정함(i가 시작도시)
    visited[i]=True
    # 시작 도시에서 시작하니 방문 체크
    solve(1,i,i,0)
    # 재귀
    visited[i]=False
    # i에서 시작하는 경우는 모두 봤으니 i는 방문 해제
print(ans)
