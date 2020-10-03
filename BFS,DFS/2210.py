import sys
input=sys.stdin.readline
# 09m 43s
# dfs 이용하는데 한 번 거쳐갔던 곳을 한 번 더 거쳐도 되므로 visit 배열 쓰지 않아야함
# 재귀로 구현해서 count가 6이 되면 하나의 수가 만들어진 것이므로 result에 추가하고 함수 종료 -> count를 안쓰고 s의 길이가 6이 되면 return시켜도 됨
# 상하좌우를 살펴야하므로 dx,dy를 사용
# 5x5에서 모든 경우를 살펴봐야함
b=[input().split() for _ in range(5)]
dx,dy=[-1,1,0,0],[0,0,-1,1]
result=set()
def dfs(r,c,s):
    if len(s)==6:
        result.add(s)
        return
    
    for k in range(4):
        rr,cc=r+dx[k],c+dy[k]
        if 0<=rr<5 and 0<=cc<5:
            dfs(rr,cc,s+b[rr][cc])
    
for i in range(5):
    for j in range(5):
        dfs(i,j,"")
print(len(result))
    
