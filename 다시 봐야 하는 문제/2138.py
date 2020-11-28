import sys
input=sys.stdin.readline
# 첫번째 전구를 눌렀을 때와 누르지 않았을 때를 나눠서 경우의 수를 구하고 최솟값을 찾는다
def change(P,T):
    C=P[:]
    press=0
    for i in range(1,N):
        if C[i-1]==T[i-1]: continue
        # 현재 전구를 누르면 이전 전구에 영향을 주므로 이전 전구가 같은지 다른지 확인한다
        # 다르면 현재 전구를 켜야하므로 press+=1 후 3개의 전구의 상태를 바꿔준다
        press+=1
        for j in range(i-1,i+2):
            if j<N: C[j]=1-C[j]
    # 위 과정을 idx가 1부터 N-1까지 반복한 뒤, 원하는 상태와 같으면 press 리턴 다르면 float('inf')를 리턴
    return press if C==T else float('inf')

N=int(input())
P=list(map(int,input().rstrip()))
T=list(map(int,input().rstrip()))
res=change(P,T)
# 첫번째 전구를 누르지 않았을 때 change 함수를 돌린다
P[0]=1-P[0]
P[1]=1-P[1]
# 첫번째 전구를 눌렀을 때 두번째 전구까지 영향을 주므로 바꾸어준 뒤, change 함수를 돌린다
res=min(res,1+change(P,T))
# 최솟값을 찾는다
print(res if res!=float('inf') else -1)




