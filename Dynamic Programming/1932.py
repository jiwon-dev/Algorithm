n=int(input())
t=[[0]+list(map(int,input().split()))+[0] for _ in range(n)]
for i in range(1,n):
    for j in range(1,len(t[i])-1):
        t[i][j]+=max(t[i-1][j-1],t[i-1][j])
print(max(t[-1]))
