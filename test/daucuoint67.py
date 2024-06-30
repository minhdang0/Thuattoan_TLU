def nguyento(n):
    if n<=2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
for _ in range (int(input())):
    a=input()
    dau,cuoi=a[0:3],a[3:]
    if nguyento(int(dau)) and nguyento(int(cuoi)):
        print("YES")
    else:
        print("NO")
           