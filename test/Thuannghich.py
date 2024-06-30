def Reversible(N):
    for i in str(N):
        if int(i) & 1 == 1:
            return False
    return str(N) == str(N)[::-1]

def Reversible_even(N):
    A=[]
    length=len(str(N))
    for i in range (22,10**length,2):
        if i<=N and Reversible(i) and len(str(i))%2==0:
            A.append(i)
        if i>N:
            break
    return A
for t in range (int(input())):
    N=int(input())
    B=Reversible_even(N)
    for i in range (len(B)):
        print(B[i],end=' ')
    print()
 
    
    