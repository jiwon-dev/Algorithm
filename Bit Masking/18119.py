import sys
input=sys.stdin.readline
# 30m 53s
# O(MN)
# 알파벳을 알고 있으면 1 없으면 0을 해당 알파벳의 비트에 표시
N,M=map(int,input().split())
dic={}
# 알파벳 배열이 같은 단어가 들어올 수 있으니 dic[비트마스크한 값]=(개수)로 시간을 줄임
total=2**26-1
# 처음에는 모든 알파벳을 알고 있으니 total=2**(알파벳 개수)-1
for _ in range(N):
    temp=0
    # 알파벳 보유 여부를 temp에 저장
    s=input().rstrip()
    for v in s:
        x=ord(v)-ord('a')
        temp|=(1<<x)
        # temp에 보유 여부 표시
        # 'a'->2^0, 'b'->2^1, 'c'->2^2, 'd'->2^3 ... 'z'->2^25
        # ex)'abc'이면 temp=2^0+2^1+2^2=7
        # 알파벳 배열이 서로 같지 않는 이상 temp는 다름(고유한 값을 가짐)
    if temp in dic: dic[temp]+=1
    # temp가 dic에 있으면 dic[temp]의 개수+1
    else: dic[temp]=1
    # 없으면 dic[temp]=(초기값=1)

items=dic.items()
# 개수를 세기 위해 items로 변환
for _ in range(M):
    o,x=input().split()
    ans=0
    # x를 지우거나 기억해냈을 때 완전히 알고 있는 단어의 개수
    if o=='1': total&=~(1<<ord(x)-ord('a'))
    # x를 지울 때:x의 자리에 맞는 비트를 0으로 만듬
    else: total|=(1<<ord(x)-ord('a'))
    # x를 기억해 낼 때:x의 자리에 맞는 비트를 1로 만듬
    # 각 쿼리마다 total은 초기화 되는 것이 아님을 주의
    for v,c in items:
        if total&v==v: ans+=c
        # items에 있는 단어 안에 모든 알파벳을 알 때, 그 단어를 완전히 안다는 의미이므로
        # (items에 있는 단어)&(현재 아는 모든 알파벳)==(items에 있는 단어)이어야 한다
    print(ans)
