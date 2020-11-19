import sys
input=sys.stdin.readline
# 10m 41s
N=int(input())
road=list(map(int,input().split()))
city=list(map(int,input().split()))

# idx가 0부터 N-2까지 돌면서 idx를 i라 했을 때,
# if city[i]<=city[i+1]이면 city[i+1]=city[i]
# 현재 주유소가 다음 주유소의 가격보다 작을 경우 다음 주유소의 가격을 현재 주유소로 바꿈 -> 0부터 N-2까지 수행
for i in range(N-1):
    if city[i]<=city[i+1]:
        city[i+1]=city[i]
ans=0
for i in range(N-1):
    ans+=city[i]*road[i]
print(ans)
