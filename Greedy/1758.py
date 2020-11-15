import sys
input=sys.stdin.readline
# 07m 02s
# 음수이면 팁을 주지 않기 때문에 내림차순으로 정렬한 뒤, 앞에서부터 입장시킨다
N=int(input())
tip=sorted([int(input()) for _ in range(N)],reverse=True)
ans=0
for i,v in enumerate(tip):
    if v-i>0: ans+=v-i
print(ans)
