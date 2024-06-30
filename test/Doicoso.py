for _ in range (int(input())):
    N,b=map(int,input().split())
    result=str()
    while N>0:
        re=N%b
        N//=b
        if re<10:
            result+=str(re)
        else:
            re-=10
            result+=chr(ord('A') + re)
    print(result[::-1])
            