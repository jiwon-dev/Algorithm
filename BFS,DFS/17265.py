import sys
from collections import deque
input=sys.stdin.readline
# 28m 29s
# 모든 경우의 수를 알아야하기 때문에 dfs 이용
# dfs(x좌표,y좌표,깊이,연산자,총 합계)
# max_value가 음수가 나올 수 있기 때문에 0이 아니라 -sys.maxsize로 초기화해야 함 -> 이거 때문에 처음에 틀림
n=int(input())
grid=[input().split() for _ in range(n)]
max_value,min_value=-sys.maxsize,sys.maxsize

def dfs(x,y,depth,char,total):
    global max_value
    global min_value
    if '0'<=grid[x][y]<='5':
        # 피연산자이면
        number=int(grid[x][y])
        # 이전 연산자(char) 종류마다 현재 숫자를 total에 계산
        if char=='+':
            total+=number
        elif char=='-':
            total-=number
        elif char=='*':
            total*=number
    else:
        # 연산자이면
        char=grid[x][y]
        # char을 현재 연산자로 바꿈
    if depth==2*n-1:
        # 깊이가 2*n-1(시작점에서 끝점까지 이동했다는 의미)이면
        max_value=max(max_value,total)
        # 최댓값 갱신
        min_value=min(min_value,total)
        # 최솟값 갱신
        # 갱신 후 함수 종료
        return
    for xx,yy in (x,y+1),(x+1,y):
        # 재귀 함수를 이용해서 다음 계산할 거 호출
        # 오른쪽과 아래쪽으로만 이동하기 때문에 depth가 2*n-1이면 시작점에서 끝점까지 이동했다는 뜻
        if 0<=xx<n and 0<=yy<n:
            dfs(xx,yy,depth+1,char,total)

dfs(0,0,1,"",int(grid[0][0]))
# 처음 total은 (0,0)에 있는 숫자
print(max_value,min_value)
