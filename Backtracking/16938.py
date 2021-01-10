import sys
input=sys.stdin.readline
# 06m 55s
# O(15C1+15C2...+15C15)
def solve(total,min_value,max_value,idx):
    # (난이도 합,가장 쉬운 문제,가장 어려운 문제,중복 선택하면 안되니 idx부터 N까지 하도록 하는 인자)
    global ans
    if L<=total<=R and max_value-min_value>=X: ans+=1
    # 몇 개를 뽑는 제한이 없으니 모든 재귀를 돌 때마다 조건에 맞으면 ans+=1
    for i in range(idx,N):
        if not visited[i]:
            # 중복 선택 방지를 위한 visited
            visited[i]=True
            solve(total+p[i],min(min_value,p[i]),max(max_value,p[i]),i)
            visited[i]=False

INF=float('inf')
N,L,R,X=map(int,input().split())
p=list(map(int,input().split()))
visited=[False]*N
ans=0
solve(0,INF,0,0)
print(ans)
