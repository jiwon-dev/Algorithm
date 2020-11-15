import sys
input=sys.stdin.readline
# 06m 15s
T=int(input())
for _ in range(T):
    box=[]
    J,N=map(int,input().split())
    for _ in range(N):
        a,b=map(int,input().split())
        box.append(a*b)
    box.sort(reverse=True)
    # 사탕을 많이->적게 담는 순(최소한으로 써야하기 때문)으로 정렬
    ans=0
    while J>0:
        # 담아야하는 사탕의 개수가 0 초과일 때만 while문 실행
        J-=box[ans]
        # 상자 선택
        ans+=1
        # 상자를 선택했으니 선택 개수 +1
    print(ans)
