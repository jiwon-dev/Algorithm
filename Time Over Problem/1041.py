import sys
input=sys.stdin.readline
# 1시간 이상
# 한 개의 면이 보이는 주사위:(N-1)*(N-2)*4+(N-2)**2개
# 두 개의 면이 보이는 주사위:(2*N-3)*4
# 세 개의 면이 보이는 주사위:4개
# 주사위의 면의 최소 합을 각각 구해서 주사위의 개수를 곱해줌
N=int(input())
D=list(map(int,input().split()))
a=min(D)
# a:한 개의 면이 보이는 주사위의 최솟값
b=c=sys.maxsize
# b:두 개의 면이 보이는 주사위 합의 최솟값, c:세 개의 면이 보이는 주사위 합의 최솟값
for i in range(6):
    for j in range(6):
        if i+j==5 or i==j: continue
        # 주사위를 만들었을 때 마주보고 있는 면은 보일 수 없다
        # 마주보는 면:i+j==5인 경우
        b=min(b,D[i]+D[j])
        # 위 조건이 아니면 b를 최솟값이 되도록 갱신
        for k in range(6):
            if i+k==5 or j+k==5 or i==k or j==k: continue
            # 두 개의 면을 선택했으므로 각각 마주보는 면은 선택할 수 없다(i+k==5 or j+k==5이면 continue)
            c=min(c,D[i]+D[j]+D[k])
            # 위 조건이 아니면 c를 최솟값이 되도록 갱신
one=(N-1)*(N-2)*4+(N-2)**2
# one은 한 면이 보이는 주사위의 개수
two=(2*N-3)*4
# two는 두 면이 보이는 주사위의 개수
print(sum(D)-max(D) if N==1 else one*a+two*b+c*4)
# 예외)N이 1일 경우 위의 공식이 통하지 않음 -> 예외 처리
