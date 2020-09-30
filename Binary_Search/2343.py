import sys
input=sys.stdin.readline
# 1시간 이상
# 처음에 정렬하고 이분 탐색해서 오답이 자꾸 나왔음
# start,last는 b의 최댓값,b의 합
# start가 b의 최댓값인 이유:만약 1이면 모든 동영상을 블루레이에 담을 수 없으니(1이면 길이 1이하의 동영상만 블루레이에 담을 수 있음)
# b의 최댓값이 모든 동영상을 블루레이에 담을 수 있는 최솟값
# last가 b의 합인 이유:블루레이의 개수가 1이라면 모든 동영상을 하나의 블루레이에 담아야하니 sum(b) 혹은 10**9를 써도 무방
n,m=map(int,input().split())
b=list(map(int,input().split()))
start,last=max(b),10**9
while start<=last:
    mid=(start+last)//2
    cnt,total=0,0
    # 블루레이 개수, 블루레이 크기
    for value in b:
        if total+value>mid:
            # 크기를 더하기 전에 mid를 넘는지 먼저 검사
            # 넘으면
            cnt+=1
            # 다른 블루레이에 나눠 담아야하므로 cnt+=1
            total=0
            # 다른 블루레이에 나눠 담아야하므로 total=0
        total+=value
        # 블루레이별로 나눈 뒤 크기를 더함
    if total!=0:
        # 마지막 동영상까지의 합이 mid보다 작을 경우
        # total은 0이 아닌데 다른 블루레이에 담아야하니 cnt+=1
        cnt+=1 
    if cnt>m:
        # 블루레이 개수가 m보다 클 경우
        start=mid+1
        # 블루레이 크기를 늘려서 더 많이 담아야 개수를 줄이므로 start=mid+1
    else:
        # 블루레이 개수가 m보다 작거나 같을 경우
        last=mid-1
        # 블루레이 크기를 줄여도 조건을 만족하는지 확인하기 위해 last=mid-1
print(start)
