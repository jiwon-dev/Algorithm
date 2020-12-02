import sys
import heapq
input=sys.stdin.readline
# 틀린 풀이: 단순히 뒤에 남은 사용 횟수가 제일 작은 것만 빼서 다시 꽂음
# 반례:3 14
# 1 4 3 2 5 4 3 2 5 3 4 2 3 4
# 올바른 풀이: 제일 늦게 쓰는 순서대로(다음 등장하는 같은 수의 idx가 큰 순서대로) 플러그를 빼야함
# 이 때, 현재 플러그가 꽂혀있는데 뒤에 쓰지 않는 것이면 -float('inf')를 우선순위 큐에 넣음
# -> 횟수가 아니라 idx로 비교해야 함
# 비어 있는 구멍이 있다면 바로 그곳에 꽂고,
# 비어 있는 구멍이 없다면 현재 사용중인 가전기기들 중 앞으로 가장 오래 뒤에(혹은 이제 사용하지 않을)
# 사용할 가전기기 플러그를 뽑고 그곳에 꽂는 걸 반복하면 됨

N,K=map(int,input().split())
E=list(map(int,input().split()))
q=[]
ans=0
def chk(k):
    for i in range(len(q)):
        if q[i][1]==E[k]:
            q.pop(i)
            heapq.heappush(q,(push(k),E[k]))
            return True
    return False

def push(i):
    for j in range(i+1,K):
        if E[i]==E[j]:
            return -j
    return -float('inf')
            
for i in range(K):
    if chk(i):
        continue
    if len(q)>=N:
        heapq.heappop(q)
        ans+=1
    res=push(i)
    heapq.heappush(q,(res,E[i]))
print(ans)
