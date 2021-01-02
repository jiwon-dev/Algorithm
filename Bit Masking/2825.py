import sys
input=sys.stdin.readline
# 1시간 이상
# 각 수를 10자리 비트로 바꾸면 입력으로 1024개까지 밖에 들어오지 않는 문제로 바뀜
def to(n):
    # 10자리 비트로 바꾸는 과정
    temp=0
    while n>0:
        temp|=(1<<(n%10))
        n//=10
    return temp

N=int(input())
cnt=[0]*1024
# 각 변환 수의 개수
for _ in range(N): cnt[to(int(input()))]+=1
# 변환 수의 개수를 더해줌

ans=0
for i in range(1024):
    ans+=cnt[i]*(cnt[i]-1)//2
    # 같은 해시값을 갖는 수들에서 nC2의 친구가 있으므로 따로 더해줌
    for j in range(i+1,1024):
        # i+1부터 1024까지 돌면서 i&j가 0이 아니면 적어도 하나의 수가 겹치므로 cnt[i]*cnt[j]를 더해줌
        if i&j: ans+=cnt[i]*cnt[j]
print(ans)
