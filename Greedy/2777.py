import sys
input=sys.stdin.readline
# 41m 21s
def cal(n):
    res=[]
    if N<10: return 1
    # N이 10미만이면 하나의 자리만으로 N을 만들 수 있으므로 1 리턴
    while True:
        com=len(res)
        # com은 res(X의 구성요소)가 변화되었는지 체크하는 변수
        for i in range(9,1,-1):
            # 9부터 2까지 나누어지면 res에 추가 -> 핵심(2부터 9까지로 하면 2,3,4,6,8,9에서 중복됨)
            if n%i==0:
                n=n//i
                # 나누어지므로 n을 i로 나눔
                res.append(i)
                # res에 추가
                break
        if n==1:
            # n이 더이상 나누어지지 않는다면 X의 구성요소의 자리 수 리턴(res의 길이)
            return len(res)
        if com==len(res):
            # 2~9까지 나누어지지 않는다면 X가 존재하지 않는다는 의미이므로 -1 리턴
            return -1

for _ in range(int(input())):
    N=int(input())
    print(cal(N))
    
