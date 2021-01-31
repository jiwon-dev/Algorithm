import sys
input=sys.stdin.readline
# 40m 15s
# 방향에 유의하며 BFS로 풀어도됨
N,M=map(int,input().split())
r,c,d=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(N)]

move={0:(-1,0),1:(0,1),2:(1,0),3:(0,-1)}
# 북동남서의 이동 좌표
visited=[[False]*M for _ in range(N)]
# 청소한 곳은 다시 방문하지 않으므로 visited로 체크
chk=True
# chk가 True이면 1단계 시작, False이면 2단계로 넘어감
ans=0
# 청소한 구역의 개수

while True:
    if chk: visited[r][c]=True; chk=False; ans+=1
    # 해당 구역을 청소해야하면 ans증가, 방문 체크, 2단계로 넘어가야하니 chk=False로 갱신
    else:
        # 2단계일 때
        for i in range(4):
            d=d-1 if d>0 else 3
            # 현재 바라보고 있는 방향으로부터 왼쪽으로 돌면서 탐색해야하니 d=d-1 이때, d<=0이면 d=3
            rr,cc=r+move[d][0],c+move[d][1]
            # 청소안한 곳으로 이동하기 위해 좌표 이동
            if not (0<=rr<N and 0<=cc<M): continue
            # 격자를 벗어나면 continue
            if not grid[rr][cc] and not visited[rr][cc]:
                # 벽이 아니고 청소하지 않은 곳이라면
                r,c=rr,cc
                # 좌표 갱신
                chk=True
                # 1단계로 넘어가야하니 chk를 True로 갱신
                break

        if chk==False:
            # 2단계에서 c,d일 경우
            rr,cc=r-move[d][0],c-move[d][1]
            # 후진은 -(x좌표),-(y좌표)
            if grid[rr][cc]:
                # 후진했을 때 벽이면
                print(ans)
                # 정답 출력 후 break
                break
            r,c=rr,cc
            # 벽이 아니면 r,c 갱신
            chk=False
            # 2단계로 넘어가야하니 chk=False로 갱신
