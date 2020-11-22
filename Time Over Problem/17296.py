import sys
input=sys.stdin.readline
# 1시간 이상
# 버튼을 전에 한 번이라도 눌렀으면 끝까지 꾹 누르고 있어야 최소가 됨
# 따라서, press(버튼을 눌렀으면 True, 아니면 False) 변수를 두어 눌렀는지 누르지 않았는지 확인
# 이 때, 0이면 누르지 않은 것으로 침
N=int(input())
B=list(map(str,input().split()))
ans=0
press=False
for v in B:
    if v=='0':
        continue
    elif str(v).find('.5')==-1:
        ans+=int(v)
    else:
        if press:
            ans+=int(float(v))
        else:
            ans+=int(float(v))+1
    press=True
print("%d"%ans)
