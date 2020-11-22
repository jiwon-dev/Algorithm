import sys
input=sys.stdin.readline
# 11m 32s
for i in range(int(input())):
    j=int(input())
    M=[list(map(int,input().split())) for _ in range(j)]
    M.sort(key=lambda x:[x[0],x[2],x[1]])
    ans=1
    time=M[0][2]
    # 이전 경기를 봤을 때 종료 시간
    day=M[0][0]
    # 첫 경기는 무조건 봐야 최대한의 경기를 볼 수 있음
    for d,s,e in M[1:]:
        if day!=d or time<=s:
            # 날이 바뀌거나 time이 현재 경기의 시작 시간보다 작거나 같으면
            ans+=1
            # 현재 경기를 볼 수 있으므로 ans+=1
            time=e
            # 현재 경기를 봤으므로 time을 현재 경기의 종료 시간으로 갱신
        day=d
        # 날짜는 계속 갱신
    print(f'Scenario #{i+1}:')
    print(ans)
    print()
