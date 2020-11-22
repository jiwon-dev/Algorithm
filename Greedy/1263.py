import sys
input=sys.stdin.readline
# 19m 12s
# 최대 시간을 정한 뒤, 줄여나가는 방식
N=int(input())
D=[list(map(int,input().split())) for _ in range(N)]
D.sort(key=lambda x:[x[1],x[0]])
# 마감 시간이 제일 촉박한 순으로 정렬 -> 시간이 적게 남은 것부터 처리해야하기 때문
ans=D[0][1]-D[0][0]
# 최대 시간은 (첫번째 일의 마감 시간)-(첫번째 일의 수행 시간)
while ans>=0:
    # 시간이 0이상일 때만 반복문 실행
    sam=ans
    # 샘플로 ans를 받고 일을 할 수 있으면 sam을 더해나감
    check=0
    # 마감 시간이 넘는 과제가 있으면 ans를 줄여야하기 때문에 체크하는 변수
    for s,e in D:
        if sam+s<=e: sam+=s
        # 마감 시간내에 처리할 수 있으면 sam+=(수행 시간)
        else:
            # 처리할 수 없으면 check=1 후 탈출
            check=1
            break
    if check==0:
        # 모든 일을 다 수행했으면 최대 시간이므로 ans 출력 후 종료
        print(ans)
        sys.exit()
    ans-=1
    # 하나라도 과제를 하지 못했다면 시간을 줄임
print(-1)
# 일을 끝마칠 수 없으므로 -1 출력
