import sys
input=sys.stdin.readline
# 18m 47s
# 스택을 활용해서 풀었음
# 스택을 써서 {}인 것을 모두 없애주면 남는 것은 {{ or }} or }{ 뿐이다
# '{{'와 '}}'는 하나의 괄호만 바꿔주면 되므로 ans+=1, '}{'는 두개의 괄호를 모두 바꿔줘야하므로 ans+=2
# 다른 풀이
# 1. stack이 비었고 '}' 문자열이면 cnt+1 하고 stack에 바꾼 '{' 를 push
# 2. stack 이 비지않았고 '}' 만나면 stack pop
# 3. 나머지는 stack에 '{' push
# 4. 모든 문자열을 탐색하고나서 stack에 쌓인 사이즈의 절반은 cnt에 더함
# 이렇게 되면 모든 문자열을 탐색하고 나면 스택에는 여는 괄호만 남아있거나 비어있게 된다
# 그래서 반틈을 닫는 괄호로 바꾸어주면 된다
idx=1
while True:
    s=input().rstrip()
    if s[0]=='-': break
    stk=[]
    for v in s:
        if v=='{': stk.append('{')
        elif stk and stk[-1]=='{': stk.pop()
        else: stk.append('}')
    ans=0
    for i in range(0,len(stk),2):
        if stk[i]+stk[i+1] in ['{{','}}']: ans+=1
        else: ans+=2
    print(f'{idx}. {ans}')
    idx+=1
    
