import sys
input=sys.stdin.readline
# 25m 35s
# size로 하지 말고 N으로 받아서 N//3을 인자로 넘겨주는 것도 있
N=int(input())
grid=[list(map(int,input().split())) for _ in range(N)]
ans=[0,0,0]
# [0으로만 채워진 종이의 개수, 1로만 채워진 종이의 개수, -1로만 채워진 종이의 개수]
def recursion(x,y,size):
    # size를 줄여나가면서 종이의 개수를 카운트함
    if size==0: return
    # base condition
    cnt=[0,0,0]
    # [0의 개수, 1의 개수, -1의 개수]
    length=int(size**0.5)
    # 가로와 세로의 길이는 같으므로 size**0.5
    for i in range(x,x+length):
        for j in range(y,y+length):
            cnt[grid[i][j]]+=1
    # 종이의 size에 맞게 -1,0,1의 개수를 count함
    # size:N^2 -> N^2//9 -> N^2//81...
    for k in range(3):
        if cnt[k]==size:
            # 종이 안에 있는 -1,0,1의 개수 중 하나가 size와 같으면(하나의 숫자가 종이를 가득 채우는 경우)
            ans[k]+=1
            # 정답을 늘리고 더 이상 종이를 나눌 필요가 없으므로 return
            return
    # 어느 한 숫자로 가득 채워진 종이가 아닐 경우
    for i in range(x,length+x,length//3):
        for j in range(y,length+y,length//3):
            # 9개의 종이로 나눠야하므로 인덱스를 각각 3으로 나눔
            recursion(i,j,size//9)
            # 나눈 인덱스와 종이로 재귀 실행
recursion(0,0,N**2)
# 처음 함수 실행
print(ans[2])
print(ans[0])
print(ans[1])
            
