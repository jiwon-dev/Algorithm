import sys
input=sys.stdin.readline
# 42m 29s
# 마지막 도토리가 들어있는 상자의 번호를 가지고 이분 탐색
# start,last=a의 최솟값,b의 최댓값
N,K,D=map(int,input().split())
B=[]
start,last=float('inf'),0
for _ in range(K):
    a,b,c=map(int,input().split())
    start=min(start,a)
    last=max(last,b)
    B.append((a,b,c))
ans=0
while start<=last:
    mid=(start+last)//2
    cnt=0
    for a,b,c in B:
        if a>mid: continue
        end=min(b,mid)
        cnt+=(end-a)//c+1
        # 위의 세 줄은 밑의 두 줄을 compact하게 줄인 것(jh05013님의 코드)
        # if b<mid: cnt+=(b-a)//c+1
        # elif a<=mid: cnt+=(mid-a)//c+1
    if cnt>=D: last=mid-1
    # 마지막 상자까지의 도토리 개수가 D 이상이면 last를 줄여야 함 -> 정답은 last 앞에 있기 때문
    else: start=mid+1
    # D 미만이면 start를 늘려야함 -> 정답은 start 뒤에 있기 때문
print(start)

