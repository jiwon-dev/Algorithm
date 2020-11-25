import sys
input=sys.stdin.readline
# 1시간 이상
# 일단 높이의 합이 3의 배수가 아니면 물을 줄 수 없음 -> 2/1을 무조건 주어야 하기때문
# 3의 배수 일 때, 총 X번의 물을 준다고하면 1 증가 물뿌리개는 X번, 2 증가 물뿌리개도 X번 사용했을 것이다
# 즉, 높이의 합이 3의 배수이면서, 2만큼 성장을 X번 시킬 수 있으면 'YES'
N=int(input())
H=list(map(int,input().split()))
even=total=0
for i in range(N):
    total+=H[i]
    even+=H[i]//2
if total%3!=0: print('NO')
elif even<total//3: print('NO')
else: print('YES')
