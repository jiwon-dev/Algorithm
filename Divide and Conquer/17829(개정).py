import sys
input=sys.stdin.readline
# copy를 쓰지 않고 함수에 변경된 리스트를 넣어 사용
def solve(arr,n):
    if n==1:
        # return을 쓸려면 재귀 함수를 부를 때도 return 사용
        return arr[0][0]
    sam=[[] for _ in range(n//2)]
    for i in range(0,n,2):
        for j in range(0,n,2):
            sam[i//2].append(sorted([arr[i][j],arr[i][j+1],arr[i+1][j],arr[i+1][j+1]])[2])
    return solve(sam,n//2)
N=int(input())
grid=[list(map(int,input().split())) for _ in range(N)]
print(solve(grid,N))
