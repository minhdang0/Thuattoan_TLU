def in_decrease(n):
    temp=-1
    if len(n)<3:
        return False
    else: 
        for i in range(0,len(n)-1):
            if n[i]>=n[i+1]:
                temp=i
                break
        if temp==-1:
            return False
        for i in range (temp,len(n)-1):
            if n[i]<=n[i+1]:
                return False
    return True
for i in range(int(input())):
    N=input()
    if in_decrease(N):
        print("YES")
    else:
        print("NO")