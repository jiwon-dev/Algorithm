import sys
input=sys.stdin.readline
# 19m 49s
# 점수를 score 배열에 넣지 않고 점수가 들어가 있으면 1, 없으면 0을 체크하고 ans 변수에 더하는 방식으로 풀어도됨
N=int(input())
S=[tuple(map(int,input().split())) for _ in range(N)]
S.sort(key=lambda x:[-x[1]])
# 점수 내림차순으로 정렬
score=[0]*1001
# score[idx]=점수 -> idx날의 최대 점수

for d,w in S:
    if score[d]==0: score[d]=w
    # d날의 점수가 비었다면 내림 차순이니 무조건 최댓값의 점수가 들어감
    # score[d]=w로 갱신
    else:
        # d날의 점수가 비지 않았다면 이미 d날에 얻을 수 있는 최대 점수가 들어간 것이므로
        # d 이전의 날을 탐색해서 점수가 빈 곳이 있으면 그 날에 넣음
        for i in range(d,0,-1):
            if score[i]==0:
                score[i]=w
                break
        # 위의 for문은 d 이전의 날을 중 빈 곳을 찾아 점수 갱신
print(sum(score))
