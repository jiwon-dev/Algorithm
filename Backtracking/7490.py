import sys
input=sys.stdin.readline
# 1시간 이상
def solve(res,sign,num,n,s):
    # (총 합,부호,이전의 값,다음 연산자,수식)
    if n==N:
        # 깊이가 N이 되면 1~N까지 다 살펴본 것임
        res+=(sign*num)
        # 마지막 계산 후 res가 0이면 s 출력
        if res==0: print(s)
        return

    # 기본 구조
    # 덧셈과 뺄셈일 때만 계산
    # 빈 칸이면 계산하지 않고 num(이전의 값)값만 변화함
    solve(res,sign,num*10+(n+1),n+1,s+' '+str(n+1))
    solve(res+(num*sign),1,n+1,n+1,s+'+'+str(n+1))
    solve(res+(num*sign),-1,n+1,n+1,s+'-'+str(n+1))
for _ in range(int(input())):
    N=int(input())
    solve(0,1,1,1,"1")
    print()
