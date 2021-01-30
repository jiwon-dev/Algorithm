import sys
import itertools
input=sys.stdin.readline
# 14m
N,M=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(N)]
chicken=[(x,y) for x in range(N) for y in range(N) if grid[x][y]==2]
home=[(x,y) for x in range(N) for y in range(N) if grid[x][y]==1]

ans=float('inf')
for i in range(1,M+1):
    com=list(itertools.combinations(chicken,i))
    # 최대 M개의 집을 선택하니 1부터 M개의 집을 선택하는 모든 경우를 살펴봐야함
    for j in range(len(com)):
        # i개의 치킨집을 선택하는 경우의 수는 j개가 나옴
        sam=0
        # 모든 집에서 가장 가까운 치킨집까지의 거리의 합
        # 아래 이중 for문은 순서가 바뀌면 안됨
        for a,b in home:
            tmp=float('inf')
            for c,d in com[j]:
                tmp=min(tmp,abs(a-c)+abs(b-d))
            sam+=tmp
        ans=min(ans,sam)
print(ans)
    
