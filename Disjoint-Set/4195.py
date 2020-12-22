import sys
input=sys.stdin.readline
# 17m 26s
# 루트가 a 일때 p[a]가 -1이 아닌 p[a]=|a를 루트로 하는 set의 노드 개수|로 설정
# 주의할 점: 앞에 나왔던 친구 관계가 순서만 바껴서 또 나올 수 있음
def find(n):
    if p[n]<0: return n
    p[n]=find(p[n])
    # 경로 압축
    return p[n]

def merge(a,b):
    a=find(a);b=find(b)
    if a==b:
        # a의 루트와 b의 루트가 같을 경우에도 친구 네트워크에 몇 명이 있는지 구해야하므로 p[a] 출력 후 return
        print(-p[a])
        return
    p[a]+=p[b]
    # p[a]:루트가 a인 set의 노드 개수, p[b]:루트가 b인 set의 노드 개수
    p[b]=a
    # 두 명을 같은 네트워크로 합쳐야하므로 p[b]=a
    print(-p[a])
    # a를 루트로 하는 set의 크기 출력
    
for _ in range(int(input())):
    F=int(input())
    R=[]
    # 친구 관계를 저장하는 리스트
    dic={}
    union=set()
    # 숫자가 아닌 문자열로 주어지므로 문자열->인덱스로 변경하기 위해 집합을 사용
    for _ in range(F):
        a,b=input().split()
        union.add(a);union.add(b)
        R.append((a,b))
    for i,f in enumerate(union): dic[f]=i
    # 문자열을 인덱스(숫자)로 변경하는 과정

    p=[-1]*1000001
    # 친구 관계 수가 F라고 해서 F명의 친구가 입력으로 들어오는 것은 아님
    # 최대 200000명의 친구가 들어올 수 있는데 넉넉히 1000000으로 잡음
    for a,b in R: merge(dic[a],dic[b])
