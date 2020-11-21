import sys
input=sys.stdin.readline
# 처음에 입력받을 때, '-'를 기준으로 나눠서 입력받음
# 예를 들어, 55-50+40이면 [55,50+40]으로 나누고 '+'가 들어간 식은 계산해서 res에 넣고 아니면 그냥 넣는다
# 위의 예시에서 res=[55,90]이 되고 제일 첫 값에서 나머지 값들을 더한 값을 빼면 원하는 값이 나온다
# ex) 55+10-50+50-10 -> [55+10,50+50,10] -> 65-(100+10) -> -45
exp=input().split('-')
res=[]
for u in exp:
    p=0
    for v in u.split('+'):
       p+=int(v)
    res.append(p)
print(res[0]-sum(res[1:]))

'''n=[sum(int(x) for x in y.split('+')) for y in input().split('-')]
   print(n[0]-sum(n[1:]))'''
    
