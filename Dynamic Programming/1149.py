N=int(input())
H=[list(map(int,input().split())) for _ in range(N)]
for i in range(1,N):
    H[i][0]+=min(H[i-1][1],H[i-1][2])
    H[i][1]+=min(H[i-1][0],H[i-1][2])
    H[i][2]+=min(H[i-1][0],H[i-1][1])
print(min(H[-1]))
