import sys
input=sys.stdin.readline
# 05m 15s
# 잉크지수가 점도지수보다 낮거나 같을 때까지 칠할 수 있다
# 단, i번째 롤러를 골랐을 경우 i+1부터 칠할 수 있다
# 즉, 한 롤러를 선택했을 때 i+1부터 n-1까지의 점도지수를 모두 살펴봐야한다
# 선형탐색을 하면 O(n^2)의 시간이 걸리므로 시간 초과
# 따라서, 이분 탐색을 사용하여 O(nlogn)의 시간에 문제를 해결할 수 있도록 한다
# 이분 탐색을 쓸 수 있는 이유:점도지수 리스트는 오름차순으로 정렬되어있기 때문
n=int(input())
ink=list(map(int,input().split()))
jum=list(map(int,input().split()))
for i in range(n):
    start,last=i,n-1
    # 하나의 롤러를 골랐을 때 start는 i,last는 n-1
    while start<=last:
        # 이분 탐색 시작
        mid=(start+last)//2
        if jum[mid]<=ink[i]:
            # 점도지수가 선택한 롤러의 잉크지수보다 작거나 같을 경우
            start=mid+1
            # 최대한 많이 칠해야 하므로 더 칠할 수 있는지 확인
            # start=mid+1을 해서 탐색 범위는 줄이되, 더 많이 칠할 수 있는지 확인
        else:
            # 점도지수가 클 경우
            last=mid-1
            # 오름차순이기 때문에 mid보다 뒤에 있는 롤러는 잉크지수보다 점도지수가 큰 경우밖에 없다
            # 따라서 뒤에는 살펴 볼 필요가 없으니 last=mid-1을 해서 탐색 범위를 줄임
    print(last-i,end=' ')
    # last 인덱스가 ink[i]가 칠할 수 있는 최대 인덱스이므로 last-i를 출력
        
        
