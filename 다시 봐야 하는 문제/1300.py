import sys
input=sys.stdin.readline
# 정답이 되는 수를 가지고 이분 탐색
N,K=int(input()),int(input())
start,last=1,K
while start<=last:
    mid=(start+last)//2
    temp=0
    # mid보다 작거나 같은 수의 개수
    for i in range(1,N+1):
        temp+=min(mid//i,N)
        # 1부터 N까지 나눈 수를 계속 더해주면 temp가 된다.
        # 이때, N이하 여야 한다.
    if temp>=K:
        last=mid-1
    else:
        start=mid+1
print(start)
