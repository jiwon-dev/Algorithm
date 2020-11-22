import sys
input=sys.stdin.readline
# 10m 40s
n,k=map(int,input().split())
Q=sorted(map(int,input().split()))
ans=0
for i in range(n):
    # i가 k보다 작을 때는 i*Q[i]를 더하고 k 이상일 때는 k*Q[i]를 더함
    # 동시에 활성화할 수 있는 개수가 k개이므로 k개보다 작을 때에는 그 개수만큼 더하고 클 때는 k개 만큼 더함
    if i<k: ans+=i*Q[i]
    else: ans+=k*Q[i]
print(ans)
