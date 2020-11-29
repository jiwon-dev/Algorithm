import sys
input=sys.stdin.readline
# 45m 53s
N=int(input())
D=[list(map(str,input().rstrip())) for _ in range(N)]
ans=""

def solve(x,y,size):
    global ans
    if size==1:
        # 크기가 1이면 무조건 압축할 수 있으므로 ans에 더하고 더 이상 나눌 필요 없으므로 return
        ans+=D[x][y]
        return
    chk=0
    # 나눠야한다면 1 아니면 0
    for i in range(x,x+size):
        for j in range(y,y+size):
            if D[x][y]!=D[i][j]:
                # 다른게 있다면 나눠야하므로 chk=1
                chk=1
                break
    if chk==1:
        # 나눠야 한다면 '('를 더함
        ans+='('
        for i in range(x,x+size,size//2):
            for j in range(y,y+size,size//2):
                # 4개로 나누어 재귀 돌림
                solve(i,j,size//2)
    else:
        # 나누지 않아야한다면 ans에 더하고 더 이상 나눌 필요 없으므로 return
        ans+=D[x][y]
        return
    ans+=')'
solve(0,0,N)
print(ans)
                
    
