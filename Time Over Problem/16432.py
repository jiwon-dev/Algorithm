import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline
# 1시간 이상
# dfs 이용
n=int(input())
graph=[list(map(int,input().split()))[1:] for _ in range(n)]
visited=[[0]*len(graph[i]) for i in range(n)]
# 방문했던 곳을 다시 방문하는 것을 막기 위함
stk=[]
# 정답이 담길 배열
def dfs(day,pre):
    # dfs(현재 날,전날 준 떡 종류)
    if day==n:
        # 현재 날이 n번째 날이면
        for s in stk:print(s)
        # stk에 있는거 출력하고 종료
        sys.exit()
    for i in range(len(graph[day])):
        # 전 날과 중복되는지 비교
        v=graph[day][i]
        # v:현재 날의 떡 종류
        if not visited[day][i] and v!=pre:
            # 현재 날의 i번째 떡을 방문하지 않았고 현재 날의 떡이 전날의 떡과 다르다면
            # 호랑이에게 줄 수 있으므로 stk에 넣고 방문 표시
            stk.append(v)
            visited[day][i]=1
            dfs(day+1,v)
            # 현재 날은 떡을 줬으므로 다음 날로 넘어감 dfs(다음 날, 준 떡 종류)
            stk.pop()
            # 재귀 다 끝났는데도 stk에 있는거 출력 못했다면 pop함
dfs(0,-1)
# dfs 함수 실행
print(-1)
# 출력 못했다면 떡을 줄 수 없는 상황이므로 -1 출력
    
