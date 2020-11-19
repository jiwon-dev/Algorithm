import sys
input=sys.stdin.readline
# 정렬 후, idx가 1 차이나는 배열은 만들 수 없으므로 2 이하로 차이나는 배열을 만듦 -> 1 차이나는 배열을 만들 경우 가장 작은 원소와 가장 큰 원소가 인접하게 됨
# 후보가 될 수 있는 조합은 (0,2), (1,3), (2,4), (3,5), ..., (N-4, N-2), (N-3, N-1)
for _ in range(int(input())):
    N=int(input())
    H=sorted(map(int,input().split()))
    ans=0
    for i in range(N-2):
        ans=max(ans,abs(H[i]-H[i+2]))
    print(ans)
