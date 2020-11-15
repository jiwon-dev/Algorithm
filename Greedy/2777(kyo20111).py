for _ in range(int(input())):
    N=int(input())
    ans=0
    for i in range(9,1,-1):
        while N%i==0:
            # 나는 while문을 for문 바깥에 뒀다면 이 분은 안쪽에 두었음
            # 하나의 수를 가지고 N을 나누어지지 않을 때까지 계속 나누는 방식
            N=N//i
            ans+=1
            # 따로 리스트를 사용할 필요없이 ans 변수 하나만으로 충분 -> 어차피 개수만 필요하기 때문
    if ans==0: ans+=1
    # 1이 들어왔을 때 예외 처리
    print(ans if N==1 else -1)
