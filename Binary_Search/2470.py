import sys
input=sys.stdin.readline
# 26m
N=int(input())
W=sorted(map(int,input().split()))
# 이분탐색을 사용하기 위해 정렬함
dif=float('inf')
# 두 용액의 합이 0으로부터 얼마나 떨어져있는지 확인하기 위한 변수(절댓값임)
a,b=0,0
for i in range(N):
    # 한 용액을 선택하고 다른 용액은 이분탐색으로 찾음
    start,last=i+1,N-1
    # i번째 용액을 선택했으니 탐색 범위는 i+1~N-1
    while start<=last:
        # 이분탐색 시작
        mid=(start+last)//2
        if W[i]+W[mid]>0: last=mid-1
        # 두 용액의 합이 양수이면 오른쪽 부분에서 탐색해봤자 0에서 멀어지므로 왼쪽 부분에서 탐색하도록 last를 줄임
        else: start=mid+1
        # 음수이면 왼쪽 부분에서 탐색해봤자 0에서 멀어지므로 오른쪽 부분에서 탐색하도록 start를 늘림
        if dif>abs(W[i]+W[mid]):
            # 합의 거리가 dif보다 작으면
            dif=abs(W[i]+W[mid])
            # dif 갱신
            a,b=W[i],W[mid]
            # 답 갱신
print(a,b)
