import sys
input=sys.stdin.readline
# 07m 10s
N=int(input())
F=[tuple(map(int,input().split())) for _ in range(N)]
F.sort(key=lambda x:(x[1],x[0]))
# 종료 시간으로 오름 차순 정렬 -> 빨리 끝나는 것을 많이 선택하면 최대 개수를 선택할 수 있음
ans=1;finish=F[0][1]
# 첫번째로 끝나는 수업 선택, finish는 해당 수업이 끝나는 시간

for i in range(1,N):
    if F[i][0]>=finish:
        # 해당 수업의 시작 시간이 finish보다 크거나 같을 경우
        finish=F[i][1]
        # 해당 수업 선택했으니 ans+=1 후, finish 갱신
        ans+=1
print(ans)
