import sys
input=sys.stdin.readline
# 26m 33s
# 최대 체력을 가지고 이분 탐색
N,H=map(int,input().split())
R=[list(map(int,input().split())) for _ in range(N)]
start,last=1,10**20
while start<=last:
    mid=(start+last)//2
    f=mid
    # mid를 가지고 받은 데미지를 계산할 수 없으니 f라는 변수를 사용
    C=H
    # H를 가지고 공격력을 계산하면 공격력이 누적으로 증가하므로 C라는 변수를 사용
    chk=0
    for t,a,h in R:
        if t==1:
            # 밑의 조건문이 핵심
            if h//C<h/C:
                # 딱뎀으로 죽이지 못하고 턴을 한번 더 썼을 때 받는 데미지:소비한 턴*a
                f-=(h//C)*a
            else:
                # 딱뎀으로 몬스터를 죽였을 때 받는 데미지:(소비한 턴-1)*a
                f-=(h//C-1)*a
        else:
            # 포션일 때
            C+=a
            f=f+h if f+h<=mid else mid
            # 최대 hp를 넘으면 f=mid 아니면 f=f+h
        if f<=0:
            chk=1
            break
    if chk==0:
        last=mid-1
    else:
        start=mid+1
print(start)
            
